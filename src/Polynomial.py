p=10**9+7
mo=p

class polynomial:
    # coeff=[a0,a1,...,a(n-1)] >> f(x) = a0 + a1*x + ... + a(n-1)*x^(n-1)
    coeff=[]
    def __init__(self,ls):
        self.coeff=[i for i in ls]
        
    def show(self):
        s=''
        f=self.coeff
        n=len(f)
        for i in range(n):
            if f[n-1-i]==0:
                continue
            s+=('+' if f[n-1-i]>0 else '')+(str(f[n-1-i]) if f[n-1-i]!=1 or i==n-1 else '')+('x^'+str(n-1-i) if i!=n-1 else '')
        print(s[1:])

    def value(self,x):
        x_p=1
        rt=0
        for i in self.coeff:
            rt+=i*x_p
            x_p*=x
        return rt
            
    def mod(self):
        self.coeff=[i%mo for i in self.coeff]
        
    def add(self,poly):
        g=poly.coeff
        n=len(self.coeff)
        m=len(g)
        if n>m:
            g+=[0]*(n-m)
        else:
            self.coeff+=[0]*(m-n)
        self.coeff=[i+j for i,j in zip(self.coeff,g)]
        return self
        
    def mult(self,poly):
        if type(poly) in (int,float):
            poly=polynomial([poly])
        f=self.coeff
        g=poly.coeff
        n=len(self.coeff)
        m=len(g)
        h=[0]*(n+m-1)
        for i in range(n):
            for j in range(m):
                h[i+j]+=f[i]*g[j]
                
        self.coeff=h
        return self
        
    def div(self,poly):
        f=[i for i in self.coeff]
        g=poly.coeff
        n=len(f)
        m=len(g)
        d=[]
        if g[-1]==0:
            # error
            return None
        if m>n:
            return (0,f)
        for i in range(n-m+1):
            c=div(f[n-1-i],g[m-1])
            d+=[c]
            for j in range(m):
                f[n-1-i-j]-=c*g[m-1-j]
        return (polynomial(d[::-1]),polynomial(f[:n-m+1]))

inv=[0]*p
for i in range(p):
    for j in range(p):
        if i*j%p==1:
            inv[i]=j
            break

def p_inv(x,p):
    return inv[x]
    
def div(a,b):
    #return a/b
    return a*p_inv(b,p)%p
