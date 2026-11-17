#!/usr/bin/env python3
"""Chromium smoke, interaction, responsive and console QA for every generated collection."""
from __future__ import annotations
import json, os, re
from pathlib import Path
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
stats={"catalog_items":len(items),"apps":len(apps),"wrappers":len(wrappers),"desktop_pages":0,"mobile_pages":0,"iframes_loaded":0,"search_controls_tested":0,"select_controls_tested":0,"filter_controls_tested":0,"tabs_tested":0,"shell_controls_tested":0}
def issue(page,kind,detail): issues.append({"page":page,"kind":kind,"detail":str(detail)[:400]})
def watch(page,label):
    page.on("pageerror",lambda e:issue(label,"pageerror",e))
    page.on("console",lambda m:issue(label,"console",m.text) if m.type=="error" else None)
def slug(s): return re.sub(r"[^a-z0-9-]+","-",s.lower()).strip("-")[:65] or "collection"
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
            home=ctx.new_page(); watch(home,"home-"+name)
            response=home.goto(BASE,wait_until="domcontentloaded",timeout=30000)
            if not response or response.status>=400: issue("home","http",response.status if response else "no response")
            try: home.wait_for_function("document.querySelectorAll('#collection-grid .collection-item').length>0",timeout=15000)
            except PlaywrightTimeout: issue("home","catalogue-render","cards did not render")
            if home.locator("#collection-grid .collection-item").count()!=len(items): issue("home","catalogue-count",home.locator("#collection-grid .collection-item").count())
            overflow(home,"home-"+name)
            home.screenshot(path=str(OUT/f"home-{name}.png"),full_page=True); screenshots.append(f"home-{name}.png")
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
                home.locator("#font-select").select_option("serif")
                if home.locator("html").get_attribute("data-rr-font")!="serif": issue("home","font","serif selection not applied")
                home.locator("#text-larger").click()
                if not home.locator("html").evaluate("(e)=>parseFloat(getComputedStyle(e).getPropertyValue('--body-scale'))>1"): issue("home","text-scale","larger control did not increase scale")
                stats["shell_controls_tested"]+=4
                home.locator("#library-search").fill("")
                home.locator("#category-filters button").filter(has_text="All").first.click()
            for item in items:
                title=item.get("title") or item.get("href","untitled")
                page=ctx.new_page(); watch(page,title+"-"+name)
                try:
                    r=page.goto(BASE+item.get("href",""),wait_until="domcontentloaded",timeout=30000)
                    if not r or r.status>=400: issue(title,"http",r.status if r else "no response")
                    page.wait_for_timeout(120)
                    if not page.title().strip(): issue(title,"title","missing title")
                    if page.locator("main").count()==0: issue(title,"landmark","main landmark missing")
                    if item.get("mature"):
                        if page.locator("#age-gate").count()==0 or not page.locator("#age-gate").is_visible(): issue(title,"age-gate","18+ gate missing or hidden")
                        if "noindex" not in (page.locator('meta[name="robots"]').get_attribute("content") or ""): issue(title,"robots","mature page not noindex")
                    overflow(page,title+"-"+name)
                    frame_el=page.locator("iframe").first
                    if frame_el.count():
                        try:
                            page.wait_for_function("document.querySelector('iframe')?.contentDocument?.readyState==='complete'",timeout=12000)
                            frame_title=frame_el.evaluate("(f)=>f.contentDocument?.title||''")
                            if not frame_title.strip(): issue(title,"iframe-title","embedded app title missing")
                            stats["iframes_loaded"]+=1
                            frame=page.frames[-1] if len(page.frames)>1 else None
                            if frame: overflow(frame,title+"-iframe-"+name)
                            if name=="desktop" and not item.get("mature"):
                                # Search fields, select filters and tabs are safe, reversible test targets.
                                sh=frame_el.evaluate_handle("""f=>f.contentDocument?.querySelector('input[type=search],input[placeholder*="search" i]')""")
                                se=sh.as_element()
                                if se:
                                    try: se.fill("qa-no-result-unique"); se.fill(""); stats["search_controls_tested"]+=1
                                    except Exception as e: issue(title,"search-control",e)
                                th=frame_el.evaluate_handle("f=>f.contentDocument?.querySelector('[role=tab]')")
                                te=th.as_element()
                                if te:
                                    try: te.click(timeout=1200); stats["tabs_tested"]+=1
                                    except Exception as e: issue(title,"tab-control",e)
                                # Use Playwright Locators for native selects; ElementHandle has no locator() method.
                                if frame:
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
                                        except Exception as e: issue(title,"select-control",e)
                                # Exercise one reversible filter/view chip when present.
                                if frame:
                                    candidates=frame.locator("button,[role=button],[role=tab],.filter-btn,.filter-button,.filter-chip,.fb,.tab-btn,.nav-tab")
                                    safe=re.compile(r"^(all|any|unwatched|watched|essential(?:\s+\d+)?|blog(?:\s+films?)?(?:\s+\d+)?|films?(?:\s+\d+)?|anime(?:\s+\d+)?|manga(?:\s+\d+)?|books?(?:\s+\d+)?|nature|emotion(?:\s*&\s*mood)?|light(?:\s*&\s*atmosphere)?|urban(?:\s*&\s*travel)?|still life|abstract|completed|grid|list|default|standard)(?:\s+✓)?$",re.I)
                                    for bi in range(min(candidates.count(),80)):
                                        btn=candidates.nth(bi)
                                        try:
                                            label=btn.inner_text(timeout=300).strip()
                                            if label and safe.match(label) and btn.is_visible() and btn.is_enabled():
                                                btn.click(timeout=1200)
                                                stats["filter_controls_tested"]+=1
                                                break
                                        except Exception: pass
                                toggle=page.locator("#rr-theme-toggle")
                                if toggle.count():
                                    toggle.click(); page.wait_for_timeout(80)
                                    pt=page.locator("html").get_attribute("data-theme")
                                    ct=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.dataset.theme")
                                    if ct and ct!=pt: issue(title,"theme-sync",f"parent={pt}, iframe={ct}")
                                font=page.locator("#rr-font-family")
                                if font.count():
                                    font.select_option("serif"); page.wait_for_timeout(80)
                                    cf=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.dataset.rrFont")
                                    if cf and cf!="serif": issue(title,"font-sync",cf)
                                scale=page.locator("#rr-text-larger")
                                if scale.count():
                                    scale.click(); page.wait_for_timeout(80)
                                    cs=frame_el.evaluate("(f)=>f.contentDocument?.documentElement?.style.getPropertyValue('--rr-scale')")
                                    if not cs: issue(title,"scale-sync","no scale value on iframe")
                        except PlaywrightTimeout:
                            issue(title,"iframe-load","iframe did not finish loading")
                    else:
                        n=len(page.locator("main").inner_text()) if page.locator("main").count() else 0
                        if n<80: issue(title,"editorial-content",f"only {n} characters in main")
                    fn=f"{slug(title)}-{name}.png"
                    page.screenshot(path=str(OUT/fn),full_page=False); screenshots.append(fn)
                except Exception as e: issue(title,"navigation-or-test",e)
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
