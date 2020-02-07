def prim_heap(edge):
    v=[0]*n
    q=g[0][:]
    heapify(q)
    v[0]=1
    rt=[]
    pre=0
    while q:
        d,(cur,num)=heappop(q)
        if v[cur]==1:
            continue
        v[cur]=1
        rt+=[num+1]
        pre=cur
        for nd,(nb,num) in g[cur]:
            if v[nb]==0:
                heappush(q,(nd,(nb,num)))
    return rt
