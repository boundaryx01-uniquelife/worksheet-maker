import sys; sys.set_int_max_str_digits(0)
import itertools, math
from collections import deque
from functools import lru_cache
# n3
from math import gcd
lcm=lambda a,b:a*b//gcd(a,b)
print('n3',lcm(12,18),3600//36,lcm(lcm(12,18),15),[x for x in range(1,200) if lcm(12,x)==60])
# n4 lockers
st=[False]*101
for s in range(1,101):
    for k in range(s,101,s):st[k]=not st[k]
op=[k for k in range(1,101) if st[k]];print('n4',op,len(op),sum(1 for d in range(1,13) if 12%d==0))
# n5
def reps(N):
    r=[]
    for k in range(2,N+1):
        t=N-k*(k-1)//2
        if t>0 and t%k==0:r.append((t//k,k))
    return r
print('n5',reps(15),[N for N in range(1,31) if not reps(N)])
# c5 catalan non-crossing matchings
def count(n):
    pts=list(range(n))
    @lru_cache(None)
    def go(l,r):
        if l>r:return 1
        tot=0
        for m in range(l+1,r+1,2):tot+=go(l+1,m-1)*go(m+1,r)
        return tot
    return go(0,n-1)
print('c5',[count(2*k) for k in range(1,7)])
# brute check non-crossing by definition for 8 points
def nc(n):
    pts=list(range(n))
    def matchings(rem):
        if not rem:yield [];return
        a=rem[0]
        for b in rem[1:]:
            rest=[x for x in rem if x not in(a,b)]
            for m in matchings(rest):yield [(a,b)]+m
    c=0
    for m in matchings(pts):
        ok=True
        for (a,b),(c2,d) in itertools.combinations(m,2):
            if a<c2<b<d or c2<a<d<b:ok=False;break
        c+=ok
    return c
print('c5b',[nc(2*k) for k in range(1,6)])
# c3 pass
codes=list(itertools.product(range(10),repeat=3))
print('c3',len(codes),sum(1 for c in codes if len(set(c))==3),sum(1 for c in codes if len(set(c))==2),sum(1 for c in codes if len(set(c))==1))
# c4
print('c4',math.perm(12,3),math.comb(12,3),math.comb(10,1),math.comb(10,3),2*math.comb(10,2),math.comb(12,3)-math.comb(7,3)-math.comb(5,3))
# g3
A=(0,0);B=(12,0);C=(12,8);D=(0,8);M=(12,4);N=(6,8)
def ar(*p):
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))/2
print('g3',ar(A,B,M),ar(A,D,N),ar(M,C,N),ar(A,M,N))
# g5
a,b=6,8
print('g5',math.hypot(a,b),30/7,40/7,24*math.sqrt(2)/7,(a+b-10)/2)
# i4 5x5 tileable removal
def tileable(n,removed):
    cells={(r,c) for r in range(n) for c in range(n)}-set(removed)
    @lru_cache(None)
    def go(s):
        if not s:return True
        first=min(s)
        for d in ((0,1),(1,0)):
            o=(first[0]+d[0],first[1]+d[1])
            if o in s and go(s-{first,o}):return True
        return False
    return go(frozenset(cells))
good=[(r,c) for r in range(5) for c in range(5) if tileable(5,[(r,c)])]
print('i4',len(good),all((r+c)%2==0 for r,c in good),tileable(8,[(0,0),(7,7)]),tileable(8,[(0,0)]))
# i5
import random
for _ in range(5):
    xs=list(range(1,11))
    while len(xs)>1:
        i,j=random.sample(range(len(xs)),2);a,b=xs[i],xs[j]
        xs=[x for k,x in enumerate(xs) if k not in(i,j)]+[a+b+a*b]
    assert xs[0]==math.factorial(11)-1
print('i5',math.factorial(11)-1,str(math.factorial(2027)-1)[-1])
# s3
print('s3',[sum(range(1,2*n,2)) for n in range(1,6)],sum(range(1,40,2)))
# s4 beads
pat='빨파파노노노초';print('s4',pat[(20-1)%7],pat[(100-1)%7],pat[(2026-1)%7],sum(1 for k in range(100) if pat[k%7]=='노'),2026%7)
# s5 hanoi adjacent
def hanoi_adj(n):
    start=(tuple(range(n,0,-1)),(),())
    def moves(s):
        for i in range(3):
            if not s[i]:continue
            for j in (i-1,i+1):
                if 0<=j<3 and (not s[j] or s[j][-1]>s[i][-1]):
                    t=[list(x) for x in s];d=t[i].pop();t[j].append(d);yield tuple(tuple(x) for x in t)
    goal=((),(),tuple(range(n,0,-1)))
    dist={start:0};q=deque([start])
    while q:
        s=q.popleft()
        if s==goal:return dist[s]
        for t in moves(s):
            if t not in dist:dist[t]=dist[s]+1;q.append(t)
def hanoi(n):
    start=(tuple(range(n,0,-1)),(),())
    def moves(s):
        for i in range(3):
            if not s[i]:continue
            for j in range(3):
                if i!=j and (not s[j] or s[j][-1]>s[i][-1]):
                    t=[list(x) for x in s];d=t[i].pop();t[j].append(d);yield tuple(tuple(x) for x in t)
    goal=((),(),tuple(range(n,0,-1)))
    dist={start:0};q=deque([start])
    while q:
        s=q.popleft()
        if s==goal:return dist[s]
        for t in moves(s):
            if t not in dist:dist[t]=dist[s]+1;q.append(t)
print('s5',[hanoi(n) for n in range(1,6)],[hanoi_adj(n) for n in range(1,5)])
