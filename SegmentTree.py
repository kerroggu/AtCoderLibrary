## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n,0)
# Range Minimum:    sg=SegTree(n,inf,min,float('inf'))

class SegTree:
    seg=[]
    num=0  # num:n以上の最小の2のべき乗
    ide_ele=0  # 単位元
    def segfun():
        return

    def __init__(self,n,init_val,segfun=sum,ide=0):
        self.ide_ele=ide
        self.num =2**(n-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num
        self.segfun=segfun
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=segfun(self.seg[2*i+1],self.seg[2*i+2]) 
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfun(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfun(res,self.seg[p])
            if q&1 == 1:
                res = self.segfun(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfun(res,self.seg[p])
        else:
            res = self.segfun(self.segfun(res,self.seg[p]),self.seg[q])
        return res
