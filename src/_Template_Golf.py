# bfs

while Q:
 N=[]
 for c in Q:
  for z in g[c]:
   if D[z]==n:N+=z,;D[z]=D[c]+1;p[z]=c
 Q=N


# binary search
l,r=0,99**9
while~l+r:
 m=l+r>>1
 if c(m):r=m
 else:l=m
