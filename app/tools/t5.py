from playwright.sync_api import sync_playwright
import re
U='file:///tmp/claude-0/-home-claude/5c78b753-7132-54a9-b959-270ee49d840c/scratchpad/math-bank3.html'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1000,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("window.claude={use:async n=>n==='downloads'?{save:async r=>{window.__f=r;return {status:'saved'}}}:null}")
    pg.goto(U);pg.click('#a-go')
    for m,bid in (('exam','#p-exam'),('sol','#p-sol')):
        pg.click(bid);pg.wait_for_timeout(500)
        f=pg.evaluate("window.__f");open(f'dl_{m}.html','w',encoding='utf8').write(f['data']);print(f['filename'],len(f['data']))
        q=b.new_page();q.goto(f'file:///tmp/claude-0/-home-claude/5c78b753-7132-54a9-b959-270ee49d840c/scratchpad/dl_{m}.html');q.wait_for_timeout(1500)
        q.pdf(path=f'dl_{m}.pdf',format='A4',print_background=True,prefer_css_page_size=True)
        print(m,len(re.findall(rb'/Type\s*/Page[^s]',open(f'dl_{m}.pdf','rb').read())))
    print(pg.inner_text('#phint'),errs)
    b.close()
