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


# https://atcoder.jp/contests/abc258/tasks/abc258_e

# g[i]: iからの移動先の頂点
g=[g]
for _ in range(41):
    t=[-1]*n
    for i in range(n):
        t[i]=g[-1][g[-1][i]]
    g+=t,

for x in k:
    x-=1
    a=0
    for i in range(41):
        if x&1:
            a=g[i][a]
        x>>=1
    print(p[a])
