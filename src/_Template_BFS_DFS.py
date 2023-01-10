####################################################################################
# DFS
# Verified by https://atcoder.jp/contests/abc138/tasks/abc138_d
#
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

q=deque([x])
v=[None]*len(g)
v[x]=0
while q:
    c=q.pop()
    for nb in g[c]:
        if v[nb]==None:
            q.append(nb)
            v[nb]=v[c]+1

####################################################################################
## 非再帰バックトラックDFS
## Veryfied by ABC 284-E
## https://atcoder.jp/contests/abc284/tasks/abc284_e

q=deque()
q+=x,
v=[None]*n
v[x]=1

while q:
    c=q.pop()
    if c<0: # 帰りがけ
        ce=~c
        v[ce]=None
    else: # 行きがけ
        ans+=1
        ce=c
        q+=~ce,
        v[ce]=1
        for nb,d in g[ce]:
            if v[nb]==None:
                q+=nb,

####################################################################################
# BFS

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

q=deque([x])
v=[None]*len(g)
v[x]=0
while q:
    c=q.popleft()
    for nb in g[c]:
        if v[nb]==None:
            q.append(nb)
            v[nb]=v[c]+1

####################################################################################
# DFS tour for Tree

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

####################################################################################
# 01BFS
# ダイクストラみたいに探索済でも距離が更新できるなら再プッシュ
# https://atcoder.jp/contests/abc246/editorial/3702


####################################################################################
# 再帰DFSでの経路全探索
# Verified by https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d

w=I()
h=I()
mp=[]
for i in range(h):
    a=LI()
    mp+=a,

ans=0
def dfs(ls):
    global ans
    ans=max(ans,len(ls))
    r,c=ls[-1]
    for dr,dc in FourNb:
        nr=r+dr
        nc=c+dc
        if 0<=nr<h and 0<=nc<w and mp[nr][nc] and ((nr,nc) not in ls):
            mp[nr][nc]=0
            dfs(ls+[(nr,nc)])
    mp[r][c]=1

for i in range(h):
    for j in range(w):
        if mp[i][j]==1:
            mp[i][j]=0
            dfs([(i,j)])

print(ans)
