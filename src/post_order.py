## return Post-order list of the graph

def dfs_order(g):
    v=[-1]*len(g)
    post_order=[]
    for x in range(n):
        if v[x]!=-1:
            continue
        q=[~x,x]
        v[x]=0
        while q:
            c=q.pop()
            if c<0:
                post_order+=~c,
                continue
            for nb,d in g[c]:
                if v[nb]==-1:
                    v[nb]=v[c]+1
                    q+=~nb,
                    q+=nb,
    return post_order
