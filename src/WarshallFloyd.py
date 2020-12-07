
def change2mat(d): # convert neiber list typr graph to matrix type graph
    inf=float('inf')
    dist=[[0 if i==j else inf for i in range(n)] for j in range(n)]
    for i in range(n):
        for v,l in d[i]:
            dist[i][v]=l
    return dist

def wf_mat(d):  # Matrix type wf
    n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j]<d[i][j]:
                    d[i][j]=d[i][k]+d[k][j]
    return d

def wf(d,flg=True): # Flag: True = Matrix type dist, False = Edge Type dist.
    n=len(d)
    if flg:
        return wf_mat(d)
    else:
        dist=change2mat(d)
        return wf_mat(dist)
