from playwright.sync_api import sync_playwright
U='file:///tmp/claude-0/-home-claude/5c78b753-7132-54a9-b959-270ee49d840c/scratchpad/math-bank3.html'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':420,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U)
    pg.screenshot(path='u1.png')
    pg.click('#t-custom');pg.screenshot(path='u2.png')
    pg.click('#c-go');print(pg.evaluate("[...document.querySelectorAll('.prob h2')].map(e=>e.textContent)"))
    pg.click('#t-bank');pg.screenshot(path='u3.png')
    # solution mode + check boxes + save
    pg.click('#m-sol');pg.evaluate("document.querySelectorAll('.rubric')[0].querySelectorAll('input').forEach(c=>c.click())")
    print('score',pg.inner_text('#sctot'))
    pg.click('#sv');pg.click('#t-rec');print(pg.inner_text('#r-bars'))
    # auto again w/ weakness
    pg.click('#t-auto');pg.fill('#a-seed','z');pg.select_option('#a-n','3');pg.click('#a-go');print(pg.inner_text('#why')[:400])
    # import
    pg.click('#t-bank')
    import json
    pg.evaluate("document.querySelector('details summary').click()")
    pg.fill('#b-json',json.dumps([{'id':'x1','title':'테스트','topic':'geo','tag':'기하','level':'중','body':'<div class="passage"><p>t<script>alert(1)</script></p></div>','sol':'<p>s</p>','rubric':[{'t':'a','p':20}]}]))
    pg.click('#b-import');print(pg.inner_text('#b-msg'));print(pg.inner_text('#b-count'))
    print(errs)
    b.close()
