########################################################################################################################################################################
## Segment Tree ##

## Test case: ABC 146 F
## https://atcoder.jp/contests/abc146/tasks/abc146_f
## Test case: EDPC Q
## https://atcoder.jp/contests/dp/tasks/dp_q

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)
# Range Maximum:    sg=SegTree(n,-inf,max,-inf)
# Range GCD:        sg=SegTree(n,0,gcd,0)

class SegTree:
    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.size=n
        self.ide_ele=ide
        self.num=1<<(self.size-1).bit_length()
        self.table=[self.ide_ele]*2*self.num
        self.index=[0]*2*self.num
        self.lazy=[self.ide_ele]*2*self.num
        self.func=function
        #set_val
        if not hasattr(init_val,"__iter__"):
            init_val=[init_val]*self.size
        for i,val in enumerate(init_val):
            self.table[i+self.num-1]=val
            self.index[i+self.num-1]=i
        #build
        for i in range(self.num-2,-1,-1):
            self.table[i]=self.func(self.table[2*i+1],self.table[2*i+2])
            if self.table[i]==self.table[i*2+1]:
                self.index[i]=self.index[i*2+1]
            else:
                self.index[i]=self.index[i*2+2]

    def __iter__(self):
        return iter(self.table[self.num-1:self.num-1+self.size])

    def __getitem__(self,key):
        if type(key) is slice:
            a=None if key.start==None else key.start
            b=None if key.stop==None else key.stop
            c=None if key.step==None else key.step
            return self.table[self.num-1:self.num-1+self.size][slice(a,b,c)]
        else:
            return self.table[key+self.num-1]

    def __setitem__(self,key,value):
        self.update(key,value)

    def update(self,k,x):
        k+=self.num-1
        self.table[k]=x
        while k:
            k=(k-1)//2
            res=self.func(self.table[k*2+1],self.table[k*2+2])
            self.table[k]=res
            
            ## Remove if index is not needed
            if res==self.table[k*2+1]:
                self.index[k]=self.index[k*2+1]
            else:
                self.index[k]=self.index[k*2+2]
            ## Remove if index is not needed
        
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
            p=p>>1
            q=(q-1)>>1
        if p==q:
            res=self.func(res,self.table[p])
        else:
            res=self.func(self.func(res,self.table[p]),self.table[q])
        return res
    
    def query_id(self,p,q):
        if q<=p:
            return self.ide_ele
        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele
        idx=p
        while q-p>1:
            if p&1==0:
                res=self.func(res,self.table[p])
                if res==self.table[p]:
                    idx=self.index[p]
            if q&1==1:
                res=self.func(res,self.table[q])
                if res==self.table[q]:
                    idx=self.index[q]
                q-=1
            p=p>>1
            q=(q-1)>>1
        if p==q:
            res=self.func(res,self.table[p])
            if res==self.table[p]:
                idx=self.index[p]
        else:
            res=self.func(self.func(res,self.table[p]),self.table[q])
            if res==self.table[p]:
                idx=self.index[p]
            elif res==self.table[q]:
                idx=self.index[q]
        return idx

    def __str__(self):
        # 生配列を表示
        rt=self.table[self.num-1:self.num-1+self.size]
        return str(rt)
