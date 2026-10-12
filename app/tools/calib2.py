import json
from playwright.sync_api import sync_playwright
U='file:///tmp/claude-0/-home-claude/5c78b753-7132-54a9-b959-270ee49d840c/scratchpad/math-bank3.html'
bank=json.load(open('bank_all.json',encoding='utf8'))
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':688,'height':1000})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U);pg.emulate_media(media='print')
    for pr in bank:
        h=pg.evaluate("""(id)=>{renderSheet([byId(id)],'t','s',[],[],'custom');setMode('exam');
          document.querySelectorAll('.ans').forEach(a=>a.style.height='0');
          return document.querySelector('.prob').getBoundingClientRect().height}""",pr['id'])
        pr['base']=round(h,1)
        print(pr['id'],pr['level'],pr['base'])
    print(errs)
    b.close()
json.dump(bank,open('bank_all.json','w',encoding='utf8'),ensure_ascii=False)
