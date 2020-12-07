## Tested by PAST_001 L
## https://atcoder.jp/contests/past201912-open/tasks/past201912_l

from heapq import heappush,heappop,heapify

def prim(edge):
    n=len(edge)
    used=[True]*n #True:不使用
    edgelist=[]
    for node,dist in edge[0]:
        heappush(edgelist,(dist,node))
    used[0]=False
    res=0
    while edgelist:
        dist,node=heappop(edgelist)
        if not used[node]:
            continue
        used[node]=False
        for nx,nx_dist in edge[node]:
            if used[nx]:
                heappush(edgelist,(nx_dist,nx))
        res+=dist
    return res
