def topological_sort(G):
    n=len(G)
    rt=[]
    indeg=[0]*n  # counter for in-degree of vertices
    for i in range(n):
        for j in G[i]:
            indeg[j]+=1
    
    # gather vertices with 0 in-degree
    q=deque()
    for i in range(n):
        if indeg[i]==0:
            q.append(i)
    
    while q:
        c=q.popleft()
        rt.append(c)
        for nb in G[c]:
            indeg[nb]-=1
            if indeg[nb]==0:
                q.append(nb)
    return rt
