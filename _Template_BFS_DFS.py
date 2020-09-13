# x := start
# edge := 隣接リスト = [[(node_j,distance_ij), (), (),,,], [(node_j,distance_ij), (),,,],,, ]
# pr := previous node, prv := previous node's value, nx := next node, dist := distance between parent and next node

from collections import deque
def dfs(x,edge,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
    q=deque([x])
    v=[None]*len(edge)
    v[x]=root_v
    while q:
        c=q.pop()
        for nb,d in edge[c]:
            if v[nb]==None:
                q.append(nb)
                v[nb]=func(c,v[c],nb,d)
    return v

def bfs(x,edge,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
    q=deque([x])
    v=[None]*len(edge)
    v[x]=root_v
    while q:
        c=q.popleft()
        for nb,d in edge[c]:
            if v[nb]==None:
                q.append(nb)
                v[nb]=func(c,v[c],nb,d)
    return v

def dfs_tr(x,edge,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
    q=deque([x])
    v=[None]*len(edge)
    v[x]=root_v
    dfs_tr=[x]
    while q:
        c=q.pop()
        for nb,d in edge[c]:
            if v[nb]==None:
                q.append(nb)
                v[nb]=func(c,v[c],nb,d)
                dfs_tr+=nb,
    return v,dfs_tr
