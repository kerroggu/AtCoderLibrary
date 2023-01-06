## 平方分割

class SqrtDecomposition:
    def __init__(self,n,ls=None,func=max,ide=-inf):
        self.size=n
        self.table=[0]*n
        self.func=func
        self.ide=ide
        
        self.bucket_size=max(int(n**0.5),1)
        self.split_pos=[0]
        while self.split_pos[-1]+self.bucket_size<n:
            self.split_pos+=self.split_pos[-1]+self.bucket_size,
        self.bucket_count=len(self.split_pos)
        #--------- update method ---------#
        self.buchet_value=[self.ide for i in range(self.bucket_count)]
        #--------- update method ---------#
        for i in range(n):
            c=ls[i]
            self.table[i]=c
            pos=self.get_position(i)
            #--------- update method ---------#
            self.buchet_value[pos]=self.func(self.buchet_value[pos],c)
            #--------- update method ---------#
        
    def get_position(self,k):
        pos=0
        while k>=self.split_pos[pos]+self.bucket_size:
            pos+=1
            if pos==self.bucket_count-1:
                break
        return pos
    
    def update(self,k,x):
        cur_value=self.table[k]
        self.table[k]=x
        pos=self.get_position(k)
        l_bound=self.split_pos[pos]
        if pos<self.bucket_count-1:
            r_bound=self.split_pos[pos+1]
        else:
            r_bound=self.size
        #--------- update method ---------#
        self.buchet_value[pos]=self.ide
        for i in range(l_bound,r_bound):
            self.buchet_value[pos]=self.func(self.buchet_value[pos],self.table[i])
        #--------- update method ---------#
        
    def query(self,l,r):
        if l>r:
            return self.ide
        l=max(0,l)
        r=min(r,self.size)
        rt=self.ide
        pos_l=self.get_position(l)
        pos_r=self.get_position(r)
        
        #--------- update method ---------#
        if pos_l==pos_r:
            for i in range(l,r):
                rt=self.func(rt,self.table[i])
            return rt
        
        rt=self.ide
        for i in range(pos_l+1,pos_r):
            rt=self.func(rt,self.buchet_value[i])
        
        if pos_l<self.bucket_count-1:
            bound_l=self.split_pos[pos_l+1]
        else:
            bound_l=self.size
        bound_r=self.split_pos[pos_r]
        for i in range(l,bound_l):
            rt=self.func(rt,self.table[i])
        for i in range(bound_r,r):
            rt=self.func(rt,self.table[i])
        #--------- update method ---------#
        #show((l,r),x,[pos_l,pos_r],(l,bound_l),[pos_l+1,pos_r-1],(bound_r,r))
        return rt

    def __getitem__(self,k):
        return self.table[k]
    
    def __str__(self):
        return str(self.table)
