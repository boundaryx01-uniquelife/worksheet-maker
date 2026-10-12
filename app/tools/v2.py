import sys; sys.set_int_max_str_digits(0)
import itertools, math
from functools import lru_cache
from collections import deque
# N1
f=lambda n:sum(map(int,str(n)))
def g(n):
    while n>=10:n=f(n)
    return n
print('N1',f(2027),g(2027),f(98765),g(98765),[n for n in range(1,101) if g(n)==7].__len__(),g(pow(2026,2026)))
assert all(g(n)==((n-1)%9+1) for n in range(1,5000))
# N2
def reach(a,b,limit=300):
    r=set()
    for x in range(limit//a+1):
        for y in range(limit//b+1):
            if a*x+b*y<=limit:r.add(a*x+b*y)
    return r
for a,b in [(3,5),(4,7),(5,8)]:
    r=reach(a,b);un=[n for n in range(300) if n not in r];print('N2',a,b,un[-1],len(un),a*b-a-b,(a-1)*(b-1)//2, un if a==3 else '')
# C1
perm=list(itertools.permutations('ABCDEF'))
print('C1',len(perm),sum(1 for p in perm if abs(p.index('A')-p.index('B'))==1),sum(1 for p in perm if abs(p.index('A')-p.index('B'))==2),sum(1 for p in perm if p.index('A')<p.index('B')<p.index('C')))
# C2
def nonadj(n,k,circ):
    c=0
    for s in itertools.combinations(range(n),k):
        ok=all((s[i+1]-s[i])>1 for i in range(k-1))
        if circ and (s[0]+n-s[-1])<=1: ok=False
        c+=ok
    return c
print('C2',nonadj(8,3,False),nonadj(10,3,True),nonadj(12,4,True),math.comb(6,3),math.comb(6,2)+math.comb(7,3),math.comb(7,3)+math.comb(8,4))
