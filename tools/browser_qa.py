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
viewports=[("desktop",1440,1000),("mobile",390,844)]
issues=[]; screenshots=[]
stats={"catalog_items":len(items),"apps":len(apps),"wrappers":len(wrappers),"desktop_pages":0,"mobile_pages":0,"iframes_loaded":0,"search_controls_tested":0,"select_controls_tested":0,"filter_controls_tested":0,"tabs_tested":0,"shell_controls_tested":0,"direct_mature_apps_tested":0,"mature_iframe_sync_tested":0,"theme_sync_tested":0,"font_sync_tested":0,"scale_sync_tested":0}
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
          const nodes=[...document.querySelectorAll("body *")].map(el=>{
            const r=el.getBoundingClientRect(),cs=getComputedStyle(el);
            return {tag:el.tagName.toLowerCase(),id:el.id||"",cls:typeof el.className==="string"?el.className.slice(0,100):"",width:Math.round(r.width),left:Math.round(r.left),right:Math.round(r.right),scroll:el.scrollWidth,client:el.clientWidth,min:cs.minWidth,whiteSpace:cs.whiteSpace,overflowX:cs.overflowX,display:cs.display};
          }).filter(n=>n.width>0&&(n.right>w+4||n.scroll>n.client+4)).sort((a,b)=>b.right-a.right).slice(0,12);
          return {w,s,nodes};
        }""")
        if x["s"]>x["w"]+4: issue(label,"horizontal-overflow",json.dumps(x))
    except Exception as e: issue(label,"layout-check",e)
def main():
    if (len(items),len(wrappers),len(apps))!=(34,34,32):
        issue("inventory","counts",f"Expected 34/34/32; found {len(items)}/{len(wrappers)}/{len(apps)}")
    expected={x.get("href") for x in items}
    actual={p.relative_to(SITE).as_posix() for p in wrappers}
    if expected!=actual: issue("inventory","wrapper-mismatch",f"catalog-only={sorted(expected-actual)} wrappers-only={sorted(actual-expected)}")
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
                page=ctx.new_page(); watch(page,qa_name+"-"+name)
                try:
                    r=page.goto(BASE+item.get("href",""),wait_until="domcontentloaded",timeout=30000)
                    if not r or r.status>=400: issue(qa_name,"http",r.status if r else "no response")
                    page.wait_for_timeout(1000)
                    if not page.title().strip(): issue(qa_name,"title","missing title")
                    if page.locator("main").count()==0: issue(qa_name,"landmark","main landmark missing")
                    if item.get("mature"):
                        if page.locator("#age-gate").count()==0 or not page.locator("#age-gate").is_visible(): issue(qa_name,"age-gate","18+ gate missing or hidden")
                        if "noindex" not in (page.locator('meta[name="robots"]').get_attribute("content") or ""): issue(qa_name,"robots","mature page not noindex")
                    elif page.locator("#age-gate").count() and page.locator("#age-gate").is_visible():
                        issue(qa_name,"unexpected-age-gate","non-mature collection is incorrectly blocked by an 18+ gate")
                    overflow(page,qa_name+"-"+name)
                    top_fn=f"{page_slug}-{name}.png"
                    page.screenshot(path=str(OUT/top_fn),full_page=False); screenshots.append(top_fn)
                    frame_el=page.locator("iframe").first
                    if frame_el.count():
                        try:
                            # Trigger loading=lazy before waiting for the embedded app.
                            frame_el.scroll_into_view_if_needed(timeout=8000)
                            page.wait_for_function("() => { const f=document.querySelector('iframe'); return !!(f && f.contentDocument && f.contentDocument.readyState !== 'loading'); }",timeout=30000)
                            page.wait_for_timeout(250)
                            frame_title=frame_el.evaluate("(f)=>f.contentDocument?.title||''")
                            if not frame_title.strip(): issue(qa_name,"iframe-title","embedded app title missing")
                            stats["iframes_loaded"]+=1
                            frame=page.frames[-1] if len(page.frames)>1 else None
                            if frame: overflow(frame,qa_name+"-iframe-"+name)
                            if item.get("mature") and frame:
                                app_gate=frame.locator("#rr-app-age-gate")
                                if app_gate.count()==0 or not app_gate.is_visible():
                                    issue(qa_name,"direct-app-age-gate","mature iframe did not show its own 18+ gate")
                                else:
                                    page.locator("#age-confirm").click()
                                    page.wait_for_timeout(180)
                                    if app_gate.is_visible(): issue(qa_name,"age-gate-sync","wrapper confirmation did not dismiss iframe gate")
                                    else: stats["mature_iframe_sync_tested"]+=1
                            app_fn=f"{page_slug}-app-{name}.png"
                            if frame:
                                frame_box=frame_el.bounding_box()
                                if frame_box and frame_box["width"]>0 and frame_box["height"]>0:
                                    page.screenshot(path=str(OUT/app_fn),clip=frame_box)
                                else:
                                    page.screenshot(path=str(OUT/app_fn),full_page=False)
                                screenshots.append(app_fn)
                                body_text=frame.locator("body").inner_text(timeout=3000).strip()
                                if len(body_text)<100:
                                    issue(qa_name,"empty-app-content",f"embedded app body has only {len(body_text)} visible characters")
                            else:
                                issue(qa_name,"missing-app-frame","iframe frame was not available")
                            if item.get("mature") and name=="desktop" and frame:
                                src=frame_el.get_attribute("src")
                                if src:
                                    direct_ctx=browser.new_context(viewport={"width":width,"height":height},service_workers="block")
                                    direct_ctx.add_init_script("try{localStorage.removeItem('rr-age-confirmed')}catch(e){}")
                                    direct=direct_ctx.new_page(); watch(direct,qa_name+"-direct-app")
                                    direct_url=urljoin(page.url,src)
                                    dr=direct.goto(direct_url,wait_until="domcontentloaded",timeout=30000)
                                    if not dr or dr.status>=400: issue(qa_name,"direct-app-http",dr.status if dr else "no response")
                                    direct.wait_for_timeout(200)
                                    dg=direct.locator("#rr-app-age-gate")
                                    if dg.count()==0 or not dg.is_visible(): issue(qa_name,"direct-app-age-gate","direct app URL bypasses the 18+ gate")
                                    if "noindex" not in (direct.locator('meta[name="robots"]').get_attribute("content") or ""): issue(qa_name,"direct-app-robots","direct mature app missing noindex")
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
                        except PlaywrightTimeout:
                            issue(qa_name,"iframe-load",f"iframe did not reach DOM-ready state; src={frame_el.get_attribute('src')}")
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
