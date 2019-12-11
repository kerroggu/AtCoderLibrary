## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

class SegTree:

    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.n=n
        self.ide_ele=ide_ele=ide
        self.num=num=2**(n-1).bit_length()
        self.seg=seg=[self.ide_ele]*2*self.num
        self.lazy=lazy=[self.ide_ele]*2*self.num
        self.segfun=segfun=function
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val
        #built
        for i in range(self.num-2,-1,-1):
            self.seg[i]=self.segfun(self.seg[2*i+1],self.seg[2*i+2])
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfun(self.seg[k*2+1],self.seg[k*2+2])
        
        
    def evaluate(k,l,r): #遅延評価処理
        if lazy[k]!=0:
            node[k]+=lazy[k]
            if(r-l>1):
                lazy[2*k+1]+=lazy[k]//2
                lazy[2*k+2]+=lazy[k]//2

        lazy[k]=0
        
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

    def __str__(self):
        # 生配列を表示
        rt=self.seg[self.num-1:self.num-1+self.n]
        return str(rt)
