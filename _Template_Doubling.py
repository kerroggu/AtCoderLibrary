for i in range(n):
    r[i]=bisect.bisect(x,x[i]+L)-1
    
par=[r]
nx=[0]*n

for k in range(m):
    nx=[0]*n
    for i in range(n):
        nx[i]=r[r[i]]
    par.append(nx)
    r=nx

for _ in range(q):
    a,b=LI_()
    if a>b:
        a,b=b,a
    
    t=0
    for p in range(m,-1,-1):
        if par[p][a]<b:
            t+=1<<p
            a=par[p][a]
    
    print(t+1)
    
