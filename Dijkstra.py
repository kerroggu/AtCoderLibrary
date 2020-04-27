from heapq import heappush, heappop,heapify

def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else 1<<33) for i in range(n)]
    prev=[0]*n
    q=[(j,i) for i,j in enumerate(d)]
    heapify(q)
    remain=set(range(n))
    # calc
    while q:
        dist,cur=heappop(q)
        if cur not in remain:
            continue
        remain.remove(cur)
        for dst,dist in edge[cur]:
            alt=d[cur]+dist
            if alt<d[dst]:
                d[dst]=alt
                prev[dst]=cur
                heappush(q,(alt,dst))
    return d,prev
