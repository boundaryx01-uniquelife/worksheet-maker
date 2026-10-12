import re
from playwright.sync_api import sync_playwright
U='file:///tmp/claude-0/-home-claude/5c78b753-7132-54a9-b959-270ee49d840c/scratchpad/math-bank3.html'
def pages(path):
    d=open(path,'rb').read();return len(re.findall(rb'/Type\s*/Page[^s]',d))
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':900,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto(U)
    pg.fill('#a-seed','abc');pg.click('#a-go')
    print('titles',pg.evaluate("[...document.querySelectorAll('.prob h2')].map(e=>e.textContent)"))
    print('why',pg.inner_text('#why')[:600])
    pg.screenshot(path='ui_auto.png')
    pg.emulate_media(media='print')
    print('headH px',pg.evaluate("document.querySelector('.head').getBoundingClientRect().height"))
    for mode in ['exam','sol']:
        pg.evaluate(f"setMode('{mode}')")
        pg.pdf(path=f'a_{mode}.pdf',prefer_css_page_size=True,print_background=True)
        print(mode,pages(f'a_{mode}.pdf'),pg.evaluate("[...document.querySelectorAll('.prob')].map(e=>Math.round(e.getBoundingClientRect().height))"))
    print('errs',errs)
    b.close()
