n,q=LI()
a=LI()

s=int(n**0.5)-1
while (s+1)**2<=n:
    s+=1

sq=[]

for i in range(s+1):
    if i==s:
        b=a[i*s:]
    else:
        b=a[i*s:(i+1)*s]
    #parts+=b,
    c=Counter(b)
    sq+=sorted(c.items(),key=lambda x:-x[1])[:4],

def most(l,r):
    L=min(l//s,s-1)
    R=min(r//s,s)
    most_c=0
    n=r-l+1
    c=defaultdict(int)
    #show((l,r),(L,R),'call',[a[l:min((L+1)*s,r+1)]]+parts[L+1:R]+([a[max(l,R*s):r+1]]if L!=R else []))
        
    for i in range(L+1,R):
        for x,cnt in sq[i]:
            c[x]+=cnt
            if most_c<c[x]:
                most_c=c[x]
    
    for x in a[l:min((L+1)*s,r+1)]+(a[max(l,R*s):r+1] if L!=R else []):
        c[x]+=1
        if most_c<c[x]:
            most_c=c[x]

    m,z=most_c,n-most_c
    if m<=(z+m+1)//2:
        return 1
    else:
        return m-z-1 +1
