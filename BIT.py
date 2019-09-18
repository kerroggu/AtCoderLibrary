# Binary Indexed Tree
# Bit.add(i,x)    : add x at i-th value
# Bit.sum(i)      : get sum up to i-th value
# Bit.l_bound(w)  : get lower bound of index where w can be inserted

class Bit:
    def __init__(self,n):
        self.size=n
        self.m=len(bin(self.size))-2
        self.arr=[0]*(2**self.m+1)
        
    def __str__(self):
        return str(self.arr)
        
    def add(self,i,x):
        k=0
        while i<=self.size:
            k+=1
            self.arr[i]+=x
            i+=i&(-i)
        return
    
    def sum(self,i):
        rt=0
        while i>0:
            rt+=self.arr[i]
            i-=i&(-i)
        return rt
    
    def l_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<self.size and self.arr[x+k]<w:
                w-=self.arr[x+k]
                x+=k
            k//=2
        return x+1
        
    def u_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<self.size and self.arr[x+k]<=w:
                w-=self.arr[x+k]
                x+=k
            k//=2
        return x+1
        
class Bit0(Bit):
    def add(self,j,x):
        super().add(j+1,x)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)
    def u_bound(self,w):
        return max(super().u_bound(w)-1,0)

class Multiset(Bit0):
    def __init__(self,max_v):
        super().__init__(max_v)
    def insert(self,x):
        super().add(x,1)
    def find(self,x):
        return super().l_bound(super().sum(x))
    def __str__(self):
        return str(self.arr)
