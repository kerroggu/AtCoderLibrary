## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

class SegTree:
    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.size=n
        self.ide_ele=ide
        self.num=2**(self.size-1).bit_length()
        self.table=[self.ide_ele]*2*self.num
        self.lazy=[self.ide_ele]*2*self.num
        self.func=function
        #set_val
        if not hasattr(init_val,"__iter__"):
            init_val=[init_val]*self.size
        for i,val in enumerate(init_val):
            self.table[i+self.num-1]=val
        #built
        for i in range(self.num-2,-1,-1):
            self.table[i]=self.func(self.table[2*i+1],self.table[2*i+2])
    
    def update(self,k,x):
        k+=self.num-1
        self.table[k]=x
        while k:
            k=(k-1)//2
            self.table[k]=self.func(self.table[k*2+1],self.table[k*2+2])
        
        
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
        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1==0:
                res=self.func(res,self.table[p])
            if q&1==1:
                res=self.func(res,self.table[q])
                q-=1
            p=p//2
            q=(q-1)//2
        if p==q:
            res=self.func(res,self.table[p])
        else:
            res=self.func(self.func(res,self.table[p]),self.table[q])
        return res

    def __str__(self):
        # 生配列を表示
        rt=self.table[self.num-1:self.num-1+self.size]
        return str(rt)
