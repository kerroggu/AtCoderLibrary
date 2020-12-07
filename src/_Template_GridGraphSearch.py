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
    return [i for i,j in d],prev

def cv(i,j):
    return i*w+j
def rcv(x):
    return x//w,x%w

h,w,T=LI()
mp=[]
for i in range(h):
    mp.append(input())
    if 'S' in mp[i]:
        sh,sw=i,mp[i].index('S')
    if 'G' in mp[i]:
        gh,gw=i,mp[i].index('G')

S=cv(sh,sw)
G=cv(gh,gw)

n=h*w

def check(k):
    g=[[] for i in range(n)]
    dd=[(0,1),(1,0),(0,-1),(-1,0)]#+[(1,1),(1,-1),(-1,-1),(-1,1)]
    for t in range(n):
        i,j=rcv(t)
        for di,dj in dd:
            if 0<=i+di<h and 0<=j+dj<w:
                dist=k if mp[i][j]=='#' else 1
                g[t].append((cv(i+di,j+dj),dist))
                
                dist=k if mp[i+di][j+dj]=='#' else 1
                g[cv(i+di,j+dj)].append((cv(i+di,j+dj),dist))
    return dijkstra(g,S)[0][G]
