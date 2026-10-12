import json
t=open('app_tpl.html',encoding='utf8').read();c=open('sheet.css',encoding='utf8').read()
bank=json.load(open('bank_all.json',encoding='utf8'))
open('math-bank3.html','w',encoding='utf8').write(t.replace('/*CSS*/',c).replace('/*BANK*/',json.dumps(bank,ensure_ascii=False)))
print('built',len(bank))
