## Verified by ABC 215-G
## https://atcoder.jp/contests/abc215/tasks/abc215_g

class Comb:
    def __init__(self,n,mo=10**9+7):
        self.mo=mo
        self.fac=[0]*(n+1)
        self.inv=[1]*(n+1)
        self.fac[0]=1
        self.fact(n)
        for i in range(1,n+1):
            self.fac[i]=i*self.fac[i-1]%self.mo
            self.inv[n]*=i
            self.inv[n]%=self.mo
        self.inv[n]=pow(self.inv[n],self.mo-2,self.mo)
        for i in range(1,n):
            self.inv[n-i]=self.inv[n-i+1]*(n-i+1)%self.mo
        return
    
    def fact(self,n):
        return self.fac[n]
        
    def invf(self,n):
        return self.inv[n]

    def comb(self,x,y):
        if y<0 or y>x:
            return 0
        return self.fac[x]*self.inv[x-y]*self.inv[y]%self.mo

    def rcomb(self,x,y):
        if y<0 or y>x:
            return 0
        return self.inv[x]*self.fac[x-y]*self.fac[y]%self.mo

    def cat(self,x):
        if x<0:
            return 0
        return self.fac[2*x]*self.inv[x]*self.inv[x+1]%self.mo

def Golf_Comb(x,y,n=10**5,M=10**9+7):
    M=10**9+7
    F=[1]
    for i in range(n):F+=F[i]*-~i%M,
    C=lambda A,B:F[A]*pow(F[A-B]*F[B],M-2,M)%M
    return C(x,y)
