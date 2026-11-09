import json, sys, re
from playwright.sync_api import sync_playwright
URL="http://localhost:8765/index.html"
res={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    for name,w,h in [("m375",375,812),("d1440",1440,900)]:
        ctx=b.new_context(viewport={"width":w,"height":h},device_scale_factor=1)
        pg=ctx.new_page(); errs=[]; reqs=[]
        pg.on("console",lambda m,e=errs: e.append(m.text) if m.type in("error","warning") else None)
        pg.on("pageerror",lambda e,l=errs: l.append("PAGEERROR "+str(e)))
        pg.on("requestfailed",lambda r,l=errs: l.append("REQFAIL "+r.url))
        pg.on("request",lambda r,l=reqs: l.append(r.url))
        pg.goto(URL); pg.wait_for_selector("#tbody tr.r"); pg.wait_for_timeout(500)
        r={}
        n=lambda: int(re.search(r"of (\d+) matching",pg.inner_text("#count")).group(1))
        r["scrollWidth"]=pg.evaluate("document.documentElement.scrollWidth"); r["clientWidth"]=pg.evaluate("document.documentElement.clientWidth")
        r["rows"]=pg.locator("#tbody tr.r").count(); r["matching"]=n(); r["more_btn"]=pg.locator("#more").count()
        # goto beyond page one before touching filters
        pg.locator("details.tllist summary").click(); pg.locator('#tllist [data-goto="UK-001"]').first.click(); pg.wait_for_timeout(300); r["goto_beyond_page"]=pg.locator("#d-UK-001").is_visible(); r["rows_after_goto"]=pg.locator("#tbody tr.r").count()
        pg.reload(); pg.wait_for_selector("#tbody tr.r")
        r["external_requests"]=[u for u in reqs if not u.startswith("http://localhost")]
        r["fonts"]=pg.evaluate("Array.from(document.fonts).filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight+' '+f.style)")
        r["h1font"]=pg.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily")
        # overflow offenders
        r["overflow"]=pg.evaluate("""()=>{const W=document.documentElement.clientWidth;return Array.from(document.querySelectorAll('body *')).filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&b.right>W+1&&!e.closest('.tlwrap')}).slice(0,8).map(e=>e.tagName+'.'+e.className+' '+Math.round(e.getBoundingClientRect().right))}""")
        pg.screenshot(path=f"/tmp/shots/{name}_top.png")
        pg.locator("#summary").screenshot(path=f"/tmp/shots/{name}_summary.png")
        # filters
        pg.select_option("#f-jur","France"); r["france_rows"]=n()
        pg.select_option("#f-status","partly delivered"); r["france_partly"]=n()
        pg.select_option("#f-jur",""); r["partly_all"]=n()
        pg.select_option("#f-status","not checked"); r["notchecked"]=n()
        pg.select_option("#f-status",""); pg.select_option("#f-type","compute"); r["compute"]=n()
        pg.select_option("#f-type",""); pg.select_option("#f-year","2026"); r["y2026"]=n()
        pg.select_option("#f-year",""); pg.select_option("#f-tot","yes"); r["counted"]=n()
        pg.select_option("#f-tot",""); pg.fill("#f-q","isambard"); r["search_isambard"]=n()
        pg.fill("#f-q","zzzz"); r["search_none"]=pg.locator("#tbody td.empty").count()
        pg.fill("#f-q",""); r["after_clear"]=n()
        # expand detail
        pg.select_option("#f-q" if False else "#f-jur","United Kingdom"); pg.locator('[data-toggle="UK-017"]').click(); r["detail_visible"]=pg.locator("#d-UK-017").is_visible()
        pg.locator("#row-UK-017").scroll_into_view_if_needed()
        pg.locator("#ledger").screenshot(path=f"/tmp/shots/{name}_ledger_open.png")
        # goto via chip in UK-012 detail
        pg.select_option("#f-jur",""); pg.locator('details.tllist summary').click() if False else None
        pg.evaluate("document.querySelector('#timeline').scrollIntoView()")
        pg.locator('#linked [data-goto="UK-012"]').first.click(); pg.wait_for_timeout(200)
        pg.locator('#d-UK-012 [data-goto="UK-003"]').first.click(); pg.wait_for_timeout(300)
        r["goto_UK003_open"]=pg.locator("#d-UK-003").is_visible()
        pg.locator("#timeline").screenshot(path=f"/tmp/shots/{name}_timeline.png")
        pg.locator("#method").screenshot(path=f"/tmp/shots/{name}_method.png")
        # cluster click
        pg.locator("#tlsvg g.dot").nth(0).click(force=True); r["tlsel"]=pg.locator("#tlsel div").count()
        r["console"]=errs
        res[name]=r
        pg.screenshot(path=f"/tmp/shots/{name}_full.png",full_page=True)
        ctx.close()
    b.close()
print(json.dumps(res,indent=1))
