# veryfied by ABC284F
# https://atcoder.jp/contests/abc284/tasks/abc284_f

# 複数インスタンス生成してハッシュ比較する時はbaseとmodを同じにするように。(TBD)初期化時にbaseとmodをシングルトンで作る。

# sample
#
# mo=10**9+7
# b=RI(2,mo-1)
# rh=RollingHash(a,b,mo)
# rh2=RollingHash(a[::-1],rh.base,rh.mod)

class RollingHash():
    def __init__(self,s,base=None,mod=10**9+7):
        self.n=len(s)
        self.mod=mod
        if base==None:
            import random
            base=random.randint(0,mod-1)
        self.base=base
        self.pw=[1]*(self.n+1)
        self.rp=[1]*(self.n+1)
        self.hash=[0]*(self.n+1)
        
        B=pow(self.base,self.n-1,self.mod)
        rb=pow(self.base,self.mod-2,self.mod)
        self.rp[1]=rb
        self.hash[1]=s[0]*B
        for i in range(1,self.n):
            B=(B*rb)%self.mod
            self.hash[i+1]=(self.hash[i]+s[i]*B)%self.mod
            self.pw[i+1]=(self.pw[i]*self.base)%self.mod
            self.rp[i+1]=(self.rp[i]*rb)%self.mod
    
    def get(self,*args): # 引数が一つで m の時、長さmの部分列のローリングハッシュを返す。引数が2つで l,r の時、[l, r) のハッシュを返す (rは開区間)
        if len(args)==1:
            m=args[0]
            return [(self.hash[l+m] - self.hash[l])*self.pw[m]%self.mod for l in range(len(self.hash)-m)]
        else:
            l,r=args
            return (self.hash[r] - self.hash[l])*self.rp[self.n-r]%self.mod

    def concat(self,l1,r1,l2,r2): # [l1,r1) + [l2,r2) を列として見たハッシュを返す。
        return (self.get(l1,r1)*self.pw[r2-l2+1]+self.get(l2,r2) )%self.mod

    def __str__(self):
        return str(self.hash)
    
