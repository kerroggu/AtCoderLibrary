################## input ##################

###  n\n a1 a2 a3\n -> n=n,a=[a1,a2,a3]
n,*a=map(int,open(0).read().split())

###  n\n a1 a2 a3\n -> a=[a1,a2,a3] # No need 'n'
a=map(int,[*open(0)][1].split())

###  x\n y\n z\n -> a=[x,y,z]
*a,=map(int,open(0))


################## combination ##################

###  (n,k)
w=1
for i in range(k):w=w*(n-i)*pow(i+1,-1,M)%M
print(w)

################## bfs ##################
while Q:
 N=[]
 for c in Q:
  for z in g[c]:
   if D[z]==n:N+=z,;D[z]=D[c]+1;p[z]=c
 Q=N

################## binary search ##################
l,r=0,99**9
while~l+r:
 m=l+r>>1
 if c(m):r=m
 else:l=m
