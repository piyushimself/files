#!/usr/bin/env python3
"""Chromium smoke, interaction, responsive and console QA for every generated collection."""
from __future__ import annotations
import json, os, re
from pathlib import Path
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
OUT=ROOT/"browser-qa-report"
BASE=os.environ.get("QA_BASE_URL","http://127.0.0.1:4173/")
OUT.mkdir(exist_ok=True)
items=json.loads((SITE/"data/catalog.json").read_text(encoding="utf-8")).get("items",[])
apps=sorted((SITE/"apps").glob("*.html"))
wrappers=sorted((SITE/"collections").glob("*/index.html"))
viewports=[("desktop",1440,1000),("tablet",768,1024),("mobile",390,844)]
issues=[]; screenshots=[]
stats={"catalog_items":len(items),"apps":len(apps),"wrappers":len(wrappers),"desktop_pages":0,"mobile_pages":0,"iframes_loaded":0,"search_controls_tested":0,"select_controls_tested":0,"filter_controls_tested":0,"tabs_tested":0,"shell_controls_tested":0,"direct_mature_apps_tested":0,"mature_iframe_sync_tested":0,"theme_sync_tested":0,"font_sync_tested":0,"scale_sync_tested":0,"filter_disclosures_tested":0}
def issue(page,kind,detail): issues.append({"page":page,"kind":kind,"detail":str(detail)[:2000]})
def watch(page,label):
    page.on("pageerror",lambda e:issue(label,"pageerror",e))
    page.on("console",lambda m:issue(label,"console",m.text) if m.type=="error" else None)
    page.on("requestfailed",lambda r:issue(label,"requestfailed",f"{r.url} ({r.failure})") if r.url.startswith(BASE) and r.resource_type in ("document","script","stylesheet","xhr","fetch") else None)
def slug(s): return re.sub(r"[^a-z0-9-]+","-",str(s).lower()).strip("-")[:72] or "collection"
def overflow(target,label):
    try:
        x=target.evaluate("""() => {
          const w=document.documentElement.clientWidth;
          const s=Math.max(document.documentElement.scrollWidth,document.body?.scrollWidth||0);
          if(s<=w+4) return {w,s,nodes:[]};
          const nodes=[...document.querySelectorAll("body *")].map(el=>{
            const r=el.getBoundingClientRect(),cs=getComputedStyle(el);
            return {tag:el.tagName.toLowerCase(),id:el.id||"",cls:typeof el.className==="string"?el.className.slice(0,100):"",width:Math.round(r.width),left:Math.round(r.left),right:Math.round(r.right),scroll:el.scrollWidth,client:el.clientWidth,min:cs.minWidth,whiteSpace:cs.whiteSpace,overflowX:cs.overflowX,display:cs.display};
          }).filter(n=>n.width>0&&(n.right>w+4||n.scroll>n.client+4)).sort((a,b)=>b.right-a.right).slice(0,12);
          return {w,s,nodes};
        }""")
        if x["s"]>x["w"]+4: issue(label,"horizontal-overflow",json.dumps(x))
    except Exception as e: issue(label,"layout-check",e)
def mobile_tabs(target,label):
    """Check that legacy category navigation stays compact and scrollable on narrow screens."""
    try:
        result=target.evaluate("""() => {
          const tabs=document.querySelector('.tabs');
          if(!tabs) return null;
          const style=getComputedStyle(tabs);
          const w=window.innerWidth;
          const buttons=[...tabs.querySelectorAll('.tab-btn')].map(b=>{
            const r=b.getBoundingClientRect();
            return {label:(b.innerText||'').trim().slice(0,50),width:Math.round(r.width),height:Math.round(r.height)};
          });
          return {viewport:w,wrap:style.flexWrap,overflowX:style.overflowX,width:Math.round(tabs.getBoundingClientRect().width),buttons};
        }""")
        if result:
            bad=[b for b in result["buttons"] if b["height"]>56 or b["width"]>result["viewport"]*.82]
            if result["wrap"]!="nowrap" or result["overflowX"] not in ("auto","scroll") or bad:
                issue(label,"mobile-tab-layout",json.dumps({**result,"oversized":bad}))
    except Exception as e:
        issue(label,"mobile-tab-layout-check",e)
def main():
    if (len(items),len(wrappers),len(apps))!=(34,34,32):
        issue("inventory","counts",f"Expected 34/34/32; found {len(items)}/{len(wrappers)}/{len(apps)}")
    expected={x.get("href") for x in items}
    actual={p.relative_to(SITE).as_posix() for p in wrappers}
    if expected!=actual: issue("inventory","wrapper-mismatch",f"catalog-only={sorted(expected-actual)} wrappers-only={sorted(actual-expected)}")
    # Regression guard: only explicitly mature collections may receive an 18+ gate.
    expected_mature={
        "collections/sen-mood-movies/index.html",
        "collections/manhwa300/index.html",
        "collections/manhwa-300-filter-app/index.html",
        "collections/manga-index/index.html",
        "collections/taboo-comics/index.html",
        "collections/top500-adult-manga/index.html",
    }
    actual_mature={x.get("href") for x in items if x.get("mature")}
    if actual_mature!=expected_mature:
        issue("inventory","mature-classification",f"expected={sorted(expected_mature)} actual={sorted(actual_mature)}")
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        for name,width,height in viewports:
            ctx=browser.new_context(viewport={"width":width,"height":height},service_workers="block")
            ctx.add_init_script("try{localStorage.removeItem('rr-age-confirmed');localStorage.setItem('rr-theme','light')}catch(e){}")
            home=ctx.new_page(); watch(home,"home-"+name)
            response=home.goto(BASE,wait_until="domcontentloaded",timeout=30000)
            if not response or response.status>=400: issue("home","http",response.status if response else "no response")
            try: home.wait_for_function("document.querySelectorAll('#collection-grid .collection-item').length>0",timeout=15000)
            except PlaywrightTimeout: issue("home","catalogue-render","cards did not render")
            if home.locator("#collection-grid .collection-item").count()!=len(items): issue("home","catalogue-count",home.locator("#collection-grid .collection-item").count())
            overflow(home,"home-"+name)
            if name=="mobile":
                nav_state=home.locator(".top-actions").evaluate("""e=>({wrap:getComputedStyle(e).flexWrap,client:e.clientWidth,scroll:e.scrollWidth,heights:[...e.children].map(x=>Math.round(x.getBoundingClientRect().height))})""")
                if nav_state["wrap"]!="nowrap" or any(h>48 for h in nav_state["heights"]): issue("home-mobile","reader-toolbar-layout",json.dumps(nav_state))
            if name=="mobile" and frame.locator(".mc").count():
                                archive=frame.evaluate("""()=>({search:document.querySelector(".mh-search")?.getBoundingClientRect().width||0,viewport:document.documentElement.clientWidth,sort:document.querySelector("#toolbar .tb-sort")?.getBoundingClientRect().width||0,sortScroll:document.querySelector("#toolbar .tb-sort")?.scrollWidth||0,sortClient:document.querySelector("#toolbar .tb-sort")?.clientWidth||0})""")
                                if archive["search"]<archive["viewport"]*.8 or archive["sort"]>archive["viewport"]+4 or archive["sortScroll"]<=archive["sortClient"]:
                                    issue(qa_name,"manga-archive-mobile-toolbar",json.dumps(archive))
            home.screenshot(path=str(OUT/f"home-{name}.png"),full_page=False); screenshots.append(f"home-{name}.png")
            if name=="desktop":
                home.locator("#library-search").fill("manga")
                if home.locator("#collection-grid .collection-item").count()<1: issue("home","search","manga search returned no items")
                home.locator("#library-search").fill("")
                cinema=home.locator("#category-filters button").filter(has_text="Cinema").first
                if cinema.count(): cinema.click()
                else: issue("home","filter","Cinema category control missing")
                home.locator("#sort-select").select_option("az")
                initial=home.locator("html").get_attribute("data-theme")
                home.locator("#theme-toggle").click()
                if home.locator("html").get_attribute("data-theme")==initial: issue("home","theme","toggle did not change theme")
                else: stats["theme_sync_tested"]+=1
                home.wait_for_timeout(150)
                home.screenshot(path=str(OUT/"home-desktop-dark.png"),full_page=False); screenshots.append("home-desktop-dark.png")
                home.locator("#font-select").select_option("serif")
                if home.locator("html").get_attribute("data-rr-font")!="serif": issue("home","font","serif selection not applied")
                home.locator("#text-larger").click()
                if not home.locator("html").evaluate("(e)=>parseFloat(getComputedStyle(e).getPropertyValue('--body-scale'))>1"): issue("home","text-scale","larger control did not increase scale")
                stats["shell_controls_tested"]+=4
                home.locator("#library-search").fill("")
                home.locator("#category-filters button").filter(has_text="All").first.click()
            for item in items:
                title=item.get("title") or item.get("href","untitled")
                page_slug=Path(item.get("href","")).parent.name or slug(title)
                qa_name=f"{title} [{page_slug}]"
                page=ctx.new_page(); page.set_default_timeout(8000); watch(page,qa_name+"-"+name)
                # Each collection must start with the default collapsed state. The shared
                # preference is intentionally persisted, so isolate QA pages from earlier tests.
                page.add_init_script("try{localStorage.removeItem('rr-filters-open')}catch(e){}")
                try:
                    r=page.goto(BASE+item.get("href",""),wait_until="domcontentloaded",timeout=30000)
                    if not r or r.status>=400: issue(qa_name,"http",r.status if r else "no response")
                    page.wait_for_timeout(1000)
                    if not page.title().strip(): issue(qa_name,"title","missing title")
                    if page.locator("main").count()==0: issue(qa_name,"landmark","main landmark missing")
                    # Editorial article pages must lead with their title; the contents guide is a compact disclosure after it.
                    if page.locator(".reading-article").count():
                        article=page.locator(".reading-article")
                        if article.locator(".article-toc").count()!=1:
                            issue(qa_name,"article-toc","article contents disclosure missing or outside the article")
                        else:
                            order=article.evaluate("""a=>({title:a.querySelector("h1")?.compareDocumentPosition(a.querySelector(".article-toc"))||0,contents:a.querySelector(".article-toc")?.compareDocumentPosition(a.querySelector(".article-content"))||0,open:a.querySelector(".article-toc")?.open})""")
                            if not (order["title"] & 4) or not (order["contents"] & 4): issue(qa_name,"article-hierarchy","article title, then contents guide, then article body is required")
                            if order["open"]: issue(qa_name,"article-toc-default","contents guide should start collapsed")
                    if item.get("mature"):
                        if page.locator("#age-gate").count()==0 or not page.locator("#age-gate").is_visible(): issue(qa_name,"age-gate","18+ gate missing or hidden")
                        if "noindex" not in (page.locator('meta[name="robots"]').get_attribute("content") or ""): issue(qa_name,"robots","mature page not noindex")
                    elif page.locator("#age-gate").count() and page.locator("#age-gate").is_visible():
                        issue(qa_name,"unexpected-age-gate","non-mature collection is incorrectly blocked by an 18+ gate")
                    overflow(page,qa_name+"-"+name)
                    top_fn=f"{page_slug}-{name}.png"
                    page.screenshot(path=str(OUT/top_fn),full_page=False); screenshots.append(top_fn)
                    frame_el=page.locator("iframe").first
                    frame_src=""
                    frame_stage="find iframe"
                    if frame_el.count():
                        frame_stage="read iframe source"
                        try:
                            frame_src=frame_el.get_attribute("src",timeout=3000) or ""
                            # Force lazy frames to load, then inspect the actual child frame.
                            frame_stage="force iframe loading"
                            frame_el.evaluate("(f)=>{f.loading='eager'}",timeout=3000)
                            frame_stage="resolve iframe content frame"
                            frame_handle=frame_el.element_handle()
                            frame=frame_handle.content_frame() if frame_handle else None
                            if not frame:
                                issue(qa_name,"missing-app-frame","iframe element has no child browsing context")
                                continue
                            try:
                                frame_stage="wait for iframe body"
                                frame.locator("body").wait_for(state="attached",timeout=10000)
                                frame_stage="wait for rendered iframe content"
                                frame.wait_for_function("""() => {
                                  const b=document.body;
                                  if(!b) return false;
                                  const g=document.querySelector("#grid,#cardsGrid,#mangaGrid,#filmGrid,#cardGrid,#collectionGrid");
                                  const controls=b.querySelectorAll("input,select,textarea,button,canvas").length;
                                  if(g) return g.children.length>0 || controls>0;
                                  return (b.textContent||"").trim().length>=30 || controls>0;
                                }""",timeout=20000)
                            except PlaywrightTimeout as wait_error:
                                try:
                                    probe=frame.locator("body").evaluate("(b)=>({text:(b.textContent||'').trim().length,controls:b.querySelectorAll('input,select,textarea,button,canvas').length,children:b.children.length})",timeout=5000)
                                    if frame.url=="about:blank" or (probe["text"]<30 and probe["controls"]==0):
                                        issue(qa_name,"iframe-load",f"child frame remained blank; src={frame_src}; {wait_error}")
                                        continue
                                except Exception as probe_error:
                                    issue(qa_name,"iframe-load",f"child frame was not inspectable; src={frame_src}; {probe_error}")
                                    continue
                            frame_stage="read iframe title"
                            page.wait_for_timeout(250)
                            frame_title=frame_el.evaluate("(f)=>f.contentDocument?.title||''")
                            if not frame_title.strip(): issue(qa_name,"iframe-title","embedded app title missing")
                            stats["iframes_loaded"]+=1
                            app_gate=frame.locator("#rr-app-age-gate")
                            if item.get("mature") and app_gate.count() and app_gate.is_visible():
                                wrapper_gate=page.locator("#age-confirm")
                                if wrapper_gate.count() and wrapper_gate.is_visible():
                                    wrapper_gate.click()
                                    page.wait_for_timeout(180)
                            # Capture the untouched initial app state before exercising/opening disclosures.
                            try:
                                initial_box=frame_el.bounding_box()
                                if initial_box and initial_box["width"]>0 and initial_box["height"]>0:
                                    page.screenshot(path=str(OUT/f"{page_slug}-app-initial-{name}.png"),clip=initial_box)
                                    screenshots.append(f"{page_slug}-app-initial-{name}.png")
                            except Exception as e:
                                issue(qa_name,"initial-app-screenshot",e)
                            if frame.locator(".stat-n").count():
                                contrast_state=frame.evaluate("""()=>{const e=document.createElement("span");e.style.color="var(--rr-ink)";document.body.append(e);const expected=getComputedStyle(e).color;e.remove();return {actual:getComputedStyle(document.querySelector(".stat-n")).color,expected}}""")
                                if contrast_state["actual"]!=contrast_state["expected"]:
                                    issue(qa_name,"stat-foreground-contrast",json.dumps(contrast_state))
                            if name=="mobile" and frame.locator(".hero-vertical").count():
                                if frame.locator(".hero-vertical").evaluate("(e)=>getComputedStyle(e).display")!="none":
                                    issue(qa_name,"mobile-vertical-ornament","decorative vertical caption must be hidden on mobile")
                            if page_slug=="300-animated-films":
                                shown=frame.locator("#hcount").inner_text().strip() if frame.locator("#hcount").count() else ""
                                if shown!="296": issue(qa_name,"catalogue-count","animated films title/count must reflect the 296 published records")
                            filter_uis=frame.locator("details.rr-filter-disclosure")
                            if filter_uis.count():
                                for disclosure_index in range(filter_uis.count()):
                                    filter_ui=filter_uis.nth(disclosure_index)
                                    if filter_ui.evaluate("(e)=>e.open"):
                                        issue(qa_name,"filters-default-open",f"filter disclosure {disclosure_index+1} should start collapsed")
                                        continue
                                    summary=filter_ui.locator(":scope > summary")
                                    panel=filter_ui.locator(":scope > :not(summary)")
                                    before=panel.locator("input,select,textarea,button").count()
                                    summary.click()
                                    if not filter_ui.evaluate("(e)=>e.open"):
                                        issue(qa_name,"filters-open",f"filter disclosure {disclosure_index+1} did not open")
                                    after=panel.locator("input,select,textarea,button").count()
                                    if before!=after:
                                        issue(qa_name,"filters-state",f"opening filter disclosure {disclosure_index+1} changed filter controls")
                                    summary.click()
                                    if filter_ui.evaluate("(e)=>e.open"):
                                        issue(qa_name,"filters-close",f"filter disclosure {disclosure_index+1} did not close")
                                    summary.click()
                                    if not filter_ui.evaluate("(e)=>e.open"):
                                        issue(qa_name,"filters-reopen",f"filter disclosure {disclosure_index+1} did not reopen for control testing")
                                    # Keep it open so later search/select checks exercise visible controls.
                                    stats["filter_disclosures_tested"]+=1
                            else:
                                possible=frame.evaluate("""() => [...document.querySelectorAll("#filters,.arc-filters,.controls-wrap,.filter-panel,.filters-panel,.filter-container,.filter-section,.filter-wrap,.filter-bar,.filters,.toolbar,.controls,[class*=filter],[id*=filter],[class*=search],[id*=search]")].some(el => {
                                  const controls=el.querySelectorAll('input:not([type="hidden"]),select,textarea').length;
                                  const cls=String(el.className||"").toLowerCase();
                                  const words=(el.innerText||"").toLowerCase();
                                  return controls>0 && (/filter|controls-wrap|toolbar/.test(cls) || (words.match(/search|filter|country|category|curriculum|status|genre|year|sort|watched|unwatched/g)||[]).length>=2);
                                })""")
                                if possible:
                                    issue(qa_name,"filters-disclosure-missing","filter-like controls exist but disclosure was not installed")
                            frame_stage="check iframe responsive overflow"
                            overflow(frame,qa_name+"-iframe-"+name)
                            if name!="desktop": mobile_tabs(frame,qa_name+"-iframe-"+name)
                            if item.get("mature") and frame:
                                frame_stage="verify mature-content gate synchronization"
                                if app_gate.count()==0:
                                    issue(qa_name,"direct-app-age-gate","mature iframe did not show its own 18+ gate")
                                elif not app_gate.is_visible():
                                    stats["mature_iframe_sync_tested"]+=1
                                else:
                                    issue(qa_name,"age-gate-sync","wrapper confirmation did not dismiss iframe gate")
                            app_fn=f"{page_slug}-app-{name}.png"
                            if frame:
                                try:
                                    frame_box=frame_el.bounding_box()
                                    if frame_box and frame_box["width"]>0 and frame_box["height"]>0:
                                        page.screenshot(path=str(OUT/app_fn),clip=frame_box)
                                    else:
                                        raise RuntimeError("iframe has no visible bounding box")
                                except Exception as e:
                                    issue(qa_name,"iframe-screenshot",e)
                                screenshots.append(app_fn)
                                frame_stage="inspect iframe body content"
                                body_text=frame.locator("body").evaluate("(b)=>(b.textContent||'').trim().slice(0,2000)",timeout=10000)
                                visible_controls=frame.locator("body :is(input,textarea,select,button,[role=button],canvas)").count()
                                content_nodes=frame.locator("body > *:not(style):not(script):not(link)").count()
                                if len(body_text)<100 and visible_controls==0:
                                    issue(qa_name,"empty-app-content",f"embedded app body has only {len(body_text)} visible characters and no controls")
                                if content_nodes==0:
                                    issue(qa_name,"empty-app-dom","embedded app body has no rendered content elements")
                                frame_stage="check iframe data grids and accessibility"
                                for grid_selector in ("#grid","#cardsGrid","#mangaGrid","#filmGrid","#cardGrid","#collectionGrid"):
                                    grid=frame.locator(grid_selector)
                                    if grid.count() and grid.locator(":scope > *").count()==0:
                                        issue(qa_name,"empty-data-grid",f"app defines {grid_selector} but renders no collection cards")
                                hidden=frame.locator(".sr-only,.visually-hidden").first
                                if hidden.count():
                                    hidden_style=hidden.evaluate("(e)=>{const s=getComputedStyle(e);return {position:s.position,width:parseFloat(s.width),height:parseFloat(s.height),overflow:s.overflow,clipPath:s.clipPath}}")
                                    if hidden_style["position"]!="absolute" or hidden_style["width"]>2 or hidden_style["height"]>2:
                                        issue(qa_name,"screen-reader-utility-visible",json.dumps(hidden_style))
                            else:
                                issue(qa_name,"missing-app-frame","iframe frame was not available")
                            if item.get("mature") and name=="desktop" and frame:
                                src=frame_src
                                if src:
                                    direct_ctx=browser.new_context(viewport={"width":width,"height":height},service_workers="block")
                                    direct_ctx.add_init_script("try{localStorage.removeItem('rr-age-confirmed')}catch(e){}")
                                    direct=direct_ctx.new_page(); direct.set_default_timeout(8000); watch(direct,qa_name+"-direct-app")
                                    direct_url=urljoin(page.url,src)
                                    dr=direct.goto(direct_url,wait_until="domcontentloaded",timeout=30000)
                                    if not dr or dr.status>=400: issue(qa_name,"direct-app-http",dr.status if dr else "no response")
                                    direct.wait_for_timeout(200)
                                    dg=direct.locator("#rr-app-age-gate")
                                    if dg.count()==0 or not dg.is_visible(): issue(qa_name,"direct-app-age-gate","direct app URL bypasses the 18+ gate")
                                    direct_robots=direct.locator('meta[name="robots"]')
                                    if direct_robots.count()==0:
                                        issue(qa_name,"direct-app-robots","direct mature app is missing robots metadata")
                                    elif "noindex" not in (direct_robots.get_attribute("content",timeout=3000) or ""):
                                        issue(qa_name,"direct-app-robots","direct mature app is not marked noindex")
                                    if dg.count() and dg.is_visible():
                                        gate_fn=f"{page_slug}-direct-gate.png"
                                        direct.screenshot(path=str(OUT/gate_fn),full_page=False); screenshots.append(gate_fn)
                                        direct.locator("#rr-app-age-confirm").click()
                                        direct.wait_for_timeout(100)
                                        if dg.is_visible(): issue(qa_name,"direct-app-confirm","direct app age confirmation did not dismiss gate")
                                        else: stats["direct_mature_apps_tested"]+=1
                                    direct_ctx.close()
                                else: issue(qa_name,"direct-app-url","mature iframe source missing")
                            if name=="desktop":
                                frame_stage="exercise representative app controls"
                                # Safe, reversible app controls are exercised after any mature gate is confirmed.
                                sh=frame_el.evaluate_handle("""f=>f.contentDocument?.querySelector('input[type=search],input[placeholder*="search" i]')""")
                                se=sh.as_element()
                                if se:
                                    try: se.fill("qa-no-result-unique"); se.fill(""); stats["search_controls_tested"]+=1
                                    except Exception as e: issue(qa_name,"search-control",e)
                                if frame:
                                    tabs=frame.locator('[role="tab"],.tab,.tab-btn,.ntab,.vt')
                                    safe=re.compile(r"^(all(?:\s+tasks?)?|any|unwatched|watched|top\s+\d+|essential(?:\s+\d+)?|blog(?:\s+films?)?(?:\s+\d+)?|films?(?:\s+\d+)?|cinema|anime(?:\s+\d+)?|manga(?:\s+\d+)?|books?(?:\s+\d+)?|nature|emotion(?:\s*&\s*mood)?|light(?:\s*&\s*atmosphere)?|urban(?:\s*&\s*travel)?|still life|abstract|completed|grid|list|default|standard|modern|romance|drama|comedy|thriller|action|fantasy|history|poetry|painting|popular|recommended)(?:\s+✓)?$",re.I)
                                    for ti in range(min(tabs.count(),80)):
                                        tab=tabs.nth(ti)
                                        try:
                                            label=tab.inner_text(timeout=300).strip()
                                            if label and safe.match(label) and tab.is_visible() and tab.is_enabled():
                                                tab.click(timeout=1200); stats["tabs_tested"]+=1; break
                                        except Exception: pass
                                    selects=frame.locator("select")
                                    for si in range(min(selects.count(),4)):
                                        sel=selects.nth(si)
                                        try:
                                            options=sel.locator("option").evaluate_all("(os)=>os.map(o=>({v:o.value,d:o.disabled}))")
                                            old=sel.input_value()
                                            candidates=[o["v"] for o in options if not o["d"] and o["v"]!=old]
                                            if candidates:
                                                sel.select_option(candidates[0])
                                                if old is not None: sel.select_option(old)
                                                stats["select_controls_tested"]+=1
                                                break
                                        except Exception as e: issue(qa_name,"select-control",e)
                                    candidates=frame.locator("button,[role=button],.filter-btn,.filter-button,.filter-chip,.fb,.nav-tab")
                                    for bi in range(min(candidates.count(),100)):
                                        btn=candidates.nth(bi)
                                        try:
                                            label=btn.inner_text(timeout=300).strip()
                                            if label and safe.match(label) and btn.is_visible() and btn.is_enabled():
                                                btn.click(timeout=1200); stats["filter_controls_tested"]+=1; break
                                        except Exception: pass
                                toggle=page.locator("#rr-theme-toggle")
                                if toggle.count():
                                    toggle.click(); page.wait_for_timeout(120)
                                    pt=page.locator("html").get_attribute("data-theme")
                                    ct=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.dataset.theme")
                                    if ct and ct!=pt: issue(qa_name,"theme-sync",f"parent={pt}, iframe={ct}")
                                    else: stats["theme_sync_tested"]+=1
                                    page.wait_for_timeout(150)
                                    dark_fn=f"{page_slug}-dark-desktop.png"
                                    page.screenshot(path=str(OUT/dark_fn),full_page=False); screenshots.append(dark_fn)
                                font=page.locator("#rr-font-family")
                                if font.count():
                                    font.select_option("serif"); page.wait_for_timeout(80)
                                    cf=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.dataset.rrFont")
                                    if cf and cf!="serif": issue(qa_name,"font-sync",cf)
                                    else: stats["font_sync_tested"]+=1
                                scale=page.locator("#rr-text-larger")
                                if scale.count():
                                    scale.click(); page.wait_for_timeout(80)
                                    cs=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.style.getPropertyValue('--rr-scale')")
                                    if not cs: issue(qa_name,"scale-sync","no scale value on iframe")
                                    else: stats["scale_sync_tested"]+=1
                        except PlaywrightTimeout as timeout_error:
                            issue(qa_name,"iframe-inspection-timeout",f"stage={frame_stage}; src={frame_src}; {timeout_error}")
                    else:
                        n=len(page.locator("main").inner_text()) if page.locator("main").count() else 0
                        if n<80: issue(qa_name,"editorial-content",f"only {n} characters in main")
                except Exception as e: issue(qa_name,"navigation-or-test",e)
                finally: page.close()
            if name=="desktop": stats["desktop_pages"]+=len(items)
            else: stats["mobile_pages"]+=len(items)
            home.close(); ctx.close()
        browser.close()
    report={"stats":stats,"issue_count":len(issues),"issues":issues,"screenshots":screenshots}
    (OUT/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    lines=["# Chromium browser QA report",""]+[f"- {k.replace('_',' ').title()}: {v}" for k,v in stats.items()]+[f"- Issues: {len(issues)}",""]
    if issues: lines+=["## Findings",""]+[f"- **{x['page']}** — {x['kind']}: {x['detail']}" for x in issues]
    else: lines+=["All automated Chromium smoke, interaction, responsive and console checks passed."]
    lines+=["","Screenshots are included in this workflow artifact."]
    (OUT/"report.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("\n".join(lines))
    return 1 if issues else 0
if __name__=="__main__": raise SystemExit(main())
