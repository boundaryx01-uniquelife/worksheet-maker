import itertools, math
from collections import deque
from fractions import Fraction as F
# G2 fold: rectangle 12x9, A=(0,0) -> M=(6,9)
xE=F(117,12);yF=F(117,18);print('G2',xE,yF,float(xE),float(yF),float(math.sqrt(xE**2+yF**2)),float(F(13,4)*math.sqrt(13)),xE*yF/2,108-xE*yF/2)
# numeric fold check by sampling: point p; line 2x+3y=19.5; A side: 2x+3y<19.5 -> reflected over line
import random
random.seed(1)
def refl(p):
    a,b,c=2,3,-19.5
    d=(a*p[0]+b*p[1]+c)/(a*a+b*b)
    return (p[0]-2*a*d,p[1]-2*b*d)
N=600
cnt1=cnt2=0
step=1/ N
tot=0;over=0;uni=0
for i in range(12*N//10):
    for j in range(9*N//10):
        x=(i+.5)/(N/10);y=(j+.5)/(N/10)
        a=2*x+3*y-19.5
        cover=0
        if a>0: cover+=1  # stays
        # reflected points of A-side land at refl
        # count layers by area-mapping: flap (a<0) maps to refl(p) in rectangle (inside) 
        if a<0: cover_flap=refl((x,y))
cell=(1/(N/10))**2
# layers: point q in rectangle: covered by base if a(q)>0 ; covered by flap if refl(q) in rect and a(q)>0
base=flap=both=0
for i in range(12*N//10):
    for j in range(9*N//10):
        x=(i+.5)/(N/10);y=(j+.5)/(N/10)
        a=2*x+3*y-19.5
        inb= a>0
        r=refl((x,y)); inf= (a>0) and (0<=r[0]<=12 and 0<=r[1]<=9)
        base+=inb;both+= inb and inf
print('outline',base*cell,'overlap',both*cell)
# I1: |a-b| game from 1..10
@__import__('functools').lru_cache(None)
def fin(state):
    if len(state)==1: return {state[0]:()}
    res={}
    s=list(state)
    seen=set()
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            a,b=s[i],s[j]
            if (a,b) in seen: continue
            seen.add((a,b))
            r=s[:i]+s[i+1:j]+s[j+1:]+[abs(a-b)]
            for v,path in fin(tuple(sorted(r))).items():
                if v not in res: res[v]=((a,b),)+path
    return res
r=fin(tuple(range(1,11)));print('I1',sorted(r))
for v in sorted(r):print(v,r[v])
# I2: flip 3 consecutive on n coins; BFS from all T
def bfs(n,k):
    start=0;goal=(1<<n)-1
    masks=[((1<<k)-1)<<i for i in range(n-k+1)]
    d={start:0};q=deque([start])
    while q:
        s=q.popleft()
        for m in masks:
            t=s^m
            if t not in d:d[t]=d[s]+1;q.append(t)
    return d.get(goal),len(d)
for n in range(3,12):print('I2',n,'k3',bfs(n,3),'k2',bfs(n,2))
# S1 staircase matchsticks
def M(n):
    cells={(i,j) for i in range(n) for j in range(n) if i+j<n}
    edges=set()
    for (i,j) in cells:
        edges|={('h',i,j),('h',i+1,j),('v',i,j),('v',i,j+1)}
    return len(cells),len(edges)
print('S1',[M(n) for n in range(1,8)])
# S2 tilings 2xn dominoes+2x2
a=[0,1,3]
for n in range(3,12):a.append(a[-1]+2*a[-2]) if False else None
a=[None,1,3]
for n in range(3,12):a.append(a[n-1]+2*a[n-2])
print('S2',a[1:11],[(2**(n+1)+(-1)**n)//3 for n in range(1,11)])
# brute-force tilings 2xn
def tilings(n):
    @__import__('functools').lru_cache(None)
    def go(col):
        if col==n:return 1
        if col>n:return 0
        # options: vertical domino (1 col), two horizontal stacked (2 cols), 2x2 square (2 cols)
        return go(col+1)+2*go(col+2)
    return go(0)
print([tilings(n) for n in range(1,11)])
