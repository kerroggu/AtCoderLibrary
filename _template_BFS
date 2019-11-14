#vには最短距離をセット & -1 で未訪問フラグ

g=[[] for i in range(n)]
for r in range(n):
''' 隣接行列バージョン
    ri=list(input())
    for c in range(n):
        if ri[c]=='1':
            s[r][c]=1
            g[r].append((c,1))
'''
    a,b,c=LI()
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))

v=[-1]*(n)

def bfs(x):  # x スタート
    p=deque()
    p.append(x)
    v[x]=0
    while p:
        c=p.popleft()
        for i,d in g[c]:
            if v[i]==-1:
                p.append(i)
                v[i]=v[c]+d
    return

