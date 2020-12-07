# edgeを引数に二部グラフ判定

v=[-1 for i in range(n)]

def IsBipartite(edge):
    q=[0]
    v[0]=0
    while q:
        c=q.pop()
        for n in edge[c]:
            if v[n]==-1:
                q.append(n)
                v[n]=1-v[c]
            elif v[n]==v[c]:
                return False
    return True
