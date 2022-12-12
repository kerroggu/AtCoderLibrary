########################################################################################################################################################################
# Verified by
# https://atcoder.jp/contests/arc033/submissions/me
# https://atcoder.jp/contests/abc174/tasks/abc174_f
#
# speed up TIPS: delete update of el. non-use of getitem, setitem.
#
# Binary Indexed Tree     
# Bit.add(i,x)      :Add x at i-th value, the following gives the same result
#           Bit[i]+=x
# Bit.sum(i)        : get sum up to i-th value
# Bit.l_bound(w)    get bound of index where x1+x2+...+xi<w

class Bit: # 1-indexed
    def __init__(self,n,init=None):
        self.size=n
        self.m=len(bin(self.size))-2
        self.arr=[0]*(2**self.m+1)
        self.el=[0]*(2**self.m+1)
        if init!=None:
            for i in range(len(init)):
                self.add(i,init[i])
                self.el[i]=init[i]

    def __str__(self):
        a=[self.sum(i+1)-self.sum(i) for i in range(self.size)]
        return str(a)
        
    def add(self,i,x):
        if not 0<i<=self.size:return NotImplemented
        self.el[i]+=x
        while i<=self.size:
            self.arr[i]+=x
            i+=i&(-i)
        return
    
    def sum(self,i):
        if not 0<=i<=self.size:return NotImplemented
        rt=0
        while i>0:
            rt+=self.arr[i]
            i-=i&(-i)
        return rt
    
    def __getitem__(self,key):
        return self.el[key]
        #return self.sum(key+1)-self.sum(key)

    def __setitem__(self,key,value):
        self.add(key,value-self.sum(key+1)+self.sum(key))

    def l_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<=self.size and self.arr[x+k]<w:
                w-=self.arr[x+k]
                x+=k
            k>>=1
        return x+1
        
    def u_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<=self.size and self.arr[x+k]<=w:
                w-=self.arr[x+k]
                x+=k
            k>>=1
        return x+1
        
class Bit0(Bit): # 0-indexed
    def add(self,j,x):
        super().add(j+1,x)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)
    def u_bound(self,w):
        return max(super().u_bound(w)-1,0)
    def __getitem__(self,key):
        return self.el[key+1]
    
class Multiset(Bit0):
    def __init__(self,max_v):
        super().__init__(max_v)
    def insert(self,x):
        super().add(x,1)
    def find(self,x):
        return super().l_bound(super().sum(x))
    def __str__(self):
        return str(self.arr)

def compress(L):
    dc={v:i for i,v in enumerate(sorted(set(L)))}
    rdc={dc[i]:i for i in L}
    return rdc,dc
