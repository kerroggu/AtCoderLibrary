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


## https://atcoder.jp/contests/arc020/tasks/arc020_3
 
def db_f(a,l,m):
    x=a
    rt=0
    cd=1
    D=pow(10,len(str(a)),m)
    k=l.bit_length()
    for i in range(k):
        if (l>>i)&1:
            rt+=x*cd
            cd*=D
            cd%=mo
        x=x*D+x
        x%=m
        
        D=D*D%m
    return rt
