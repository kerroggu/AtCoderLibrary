## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

#-------------------------------
    
class SegTree:

    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.n=n
        self.ide_ele=ide_ele=ide
        self.num=num=2**(n-1).bit_length()
        self.data=data=[self.ide_ele]*2*self.num
        self.lazy=lazy=[self.ide_ele]*2*self.num
        self.segfun=segfun=function
        #set_val
        for i in range(n):
            self.data[i+self.num-1]=init_val
        #built
        for i in range(self.num-2,-1,-1):
            self.data[i]=self.segfun(self.data[2*i+1],self.data[2*i+2])

    def gindex(self,l, r):
        L = (l + 2*self.num) >> 1
        R = (r + 2*self.num) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range((self.n-1).bit_length()):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    # 区間[l, r)にxを加算
    def update(self,l,r,x):
        *ids, = self.gindex(l,r)
        self.propagates(*ids)

        L = 2*self.num + l; R = 2*self.num + r
        while L < R:
            if R & 1:
                R -= 1
                slef.lazy[R-1] += x; slef.data[R-1] += x
            if L & 1:
                slef.lazy[L-1] += x; slef.data[L-1] += x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            slef.data[i-1] = segfun(slef.data[2*i-1], slef.data[2*i])


    # 遅延伝搬処理
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    def query(self,l,r):
        self.propagates(*gindex(l, r))
        L = 2*self.num + l; R = 2*self.num + r
        
        if r<=l:
            return self.ide_ele
        
        res = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                res = self.segfun(res, self.data[R-1])
            if L & 1:
                res = self.segfun(res, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return res

    def __str__(self):
        # 生配列を表示
        rt=self.data[self.num-1:self.num-1+self.n]
        return str(rt)

#-------------------------------
