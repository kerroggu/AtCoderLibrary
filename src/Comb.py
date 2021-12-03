
class Comb:
    def __init__(self,n=0,mo=10**9+7):
        self.size=1
        self.mo=mo
        self.fac=[0]*self.size
        self.inv=[1]*self.size
        self.fac[0]=1
        self.extend(n+1)
        return
    
    def extend(self,mx):
        x=max(2*self.size,mx)-self.size+1
        self.fac+=[0]*x
        self.inv+=[1]*x
        for i in range(self.size,self.size+x):
            self.fac[i]=i*self.fac[i-1]%self.mo
            self.inv[-1]*=i
            self.inv[-1]%=self.mo
        self.inv[-1]=pow(self.inv[-1],self.mo-2,self.mo)
        self.inv[-1]*=self.inv[self.size-1]
        self.inv[-1]%=self.mo
        for i in range(x+self.size-1,self.size,-1):
            self.inv[i-1]=self.inv[i]*(i)%self.mo
        self.size+=x
        return
    
    def fact(self,n):
        if n>=self.size:
            self.extend(n)
        return self.fac[n]
        
    def invf(self,n):
        if n>=self.size:
            self.extend(n)
        return self.inv[n]

    def comb(self,x,y):
        if y<0 or y>x:
            return 0
        if x>=self.size:
            self.extend(x)
        return self.fac[x]*self.inv[x-y]*self.inv[y]%self.mo

    def rcomb(self,x,y):
        if y<0 or y>x:
            return 0
        if x>=self.size:
            self.extend(x)
        return self.inv[x]*self.fac[x-y]*self.fac[y]%self.mo

    def cat(self,x):
        if x<0:
            return 0
        if 2*x>self.size:
            self.extend(x)
        return self.fac[2*x]*self.inv[x]*self.inv[x+1]%self.mo

def Golf_Comb(x,y,n=10**5,M=10**9+7):
    M=10**9+7
    F=[1]
    for i in range(n):F+=F[i]*-~i%M,
    C=lambda A,B:F[A]*pow(F[A-B]*F[B],M-2,M)%M
    return C(x,y)
