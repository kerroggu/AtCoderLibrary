# bfs

while Q:
 N=[]
 for c in Q:
  for z in g[c]:
   if D[z]==n:N+=z,;D[z]=D[c]+1;p[z]=c
 Q=N
