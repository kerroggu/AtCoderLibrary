from heapq import heappush, heappop,heapify

def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf,i) for i in range(n)]
    prev=[0]*n
    q=[i for i in d]
    heapify(q)
    
    # calc
    while q:
        dist,cur=heappop(q)
        for dst,dist in edge[cur]:
            alt=d[cur][0]+dist
            if alt<d[dst][0]:
                d[dst]=(alt,dst)
                prev[dst]=cur
                heappush(q,(alt,dst))
    return d,prev
