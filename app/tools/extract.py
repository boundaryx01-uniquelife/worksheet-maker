import json,re
from bs4 import BeautifulSoup
soup=BeautifulSoup(open('mock1.html',encoding='utf8').read(),'html.parser')
meta={1:('number','중상',85),2:('combi','중',115),3:('geo','중',110),4:('inv','중',150),5:('seq','상',165)}
out=[]
for sec in soup.select('section.prob'):
    n=int(sec['data-prob']); topic,level,ah=meta[n]
    title=re.sub(r'^문제 \d+\.\s*','',sec.select_one('.prob-head h2').get_text().strip())
    tag=sec.select_one('.tag').get_text().strip()
    body=[]
    for el in sec.find('div',class_='passage').find_all_next(True,recursive=False) if False else []: pass
    kids=[c for c in sec.children if getattr(c,'name',None)]
    started=False
    for c in kids:
        cls=c.get('class') or []
        if 'passage' in cls: started=True
        if 'exam-only' in cls: break
        if started: body.append(str(c))
    sol=sec.select_one('.sol')
    rub=sol.select_one('.rubric')
    items=[]
    for lab in rub.select('label'):
        p=int(lab.input['data-pts'])
        pt=lab.select_one('.pt'); pt.extract()
        lab.input.extract()
        items.append({'t':lab.decode_contents().strip(),'p':p})
    rub.extract()
    out.append({'id':f'm1-{n}','title':title,'topic':topic,'tag':tag,'level':level,'pts':20,'min':20,'ah':ah,
      'body':''.join(body),'sol':sol.decode_contents().strip(),'rubric':items,'src':'모의고사 1회'})
json.dump(out,open('bank1.json','w',encoding='utf8'),ensure_ascii=False)
for o in out: print(o['id'],o['title'],o['level'],len(o['body']),len(o['sol']),sum(i['p'] for i in o['rubric']))
