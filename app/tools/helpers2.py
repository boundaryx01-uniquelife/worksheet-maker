import json, math, itertools, sys
sys.set_int_max_str_digits(0)
def i(x): return f'<i>{x}</i>'
def q(n,text,p): return f'<div class="q"><span class="n">({n})</span> {text} <span class="p">[{p}점]</span></div>'
def passage(*ps): return '<div class="passage">'+''.join(f'<p>{p}</p>' for p in ps)+'</div>'
def ol(*items): return '<ol>'+''.join(f'<li>{x}</li>' for x in items)+'</ol>'
def h3(t): return f'<h3>{t}</h3>'
def ans(t): return f'<p class="ans-line">{t}</p>'
def read(t): return f'<div class="read"><b>문해력 포인트.</b> {t}</div>'
def check(t,label='스스로 점검'): return f'<div class="read"><b>{label}.</b> {t}</div>'
def pit(t): return f'<div class="pitfall"><b>자주 하는 실수.</b> {t}</div>'
P=[]
def add(id,title,topic,tag,level,body,sol,rubric):
    assert sum(r[1] for r in rubric)==20,(id,sum(r[1] for r in rubric))
    P.append(dict(id=id,title=title,topic=topic,tag=tag,level=level,pts=20,min=20,ah=100,body=body,sol=sol,rubric=[{'t':t,'p':p} for t,p in rubric],src='추가 문제 세트'))

# ---------- N1 숫자 압축기 ----------
f=lambda n:sum(map(int,str(n)))
def g(n):
    while n>=10:n=f(n)
    return n
assert (f(2027),g(2027),g(98765))==(11,2,8) and sum(1 for n in range(1,101) if g(n)==7)==11 and g(pow(2026,2026))==1
