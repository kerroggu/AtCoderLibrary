from heapq import heappush, heappop,heapify

def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf) for i in range(n)]
    prev=[0]*n
    q=[(j,i) for i,j in enumerate(d)]
    heapify(q)
    v=[False]*n
    # calc
    while q:
        dist,cur=heappop(q)
        if v[cur]:
            continue
        v[cur]=True
        for dst,dist in edge[cur]:
            alt=d[cur]+dist
            if alt<d[dst]:
                d[dst]=alt
                prev[dst]=cur
                heappush(q,(alt,dst))
    return d,prev


def golf_dijkstra():
 from heapq import*;n,m,k,*t=map(int,open(0).read().split());P=[t[i*3:i*3+3]for i in range(m)];s=t[3*m:];g=[[]for _ in' '*-~n];q=[(0,i)for i in s];v=[1]*-~n
 for a,b,l in P:g[a]+=(b,l),;g[b]+=(a,l),
 D=[1e9]*-~n
 for i in s:D[i]=0
 while q:
  d,c=heappop(q)
  if v[c]:
   for N,d in g[c]:
    A=D[c]+d;v[c]=0
    if A<D[N]:D[N]=A;heappush(q,(A,N))
