## 平方分割

class sqrt_divide:
    def __init__(self,n,ls=None):
        self.size=n
        self.table=[0]*n
        
        self.split_size=max(int(n**0.5),1)
        self.split_pos=[0]
        while self.split_pos[-1]+self.split_size<n:
            self.split_pos+=self.split_pos[-1]+self.split_size,
        self.split_count=len(self.split_pos)
        self.dc=[defaultdict(int) for i in range(self.split_count)]
        for i in range(n):
            c=ls[i]
            self.table[i]=c
            pos=self.get_position(i)
            self.dc[pos][c]+=1
        
    def get_position(self,k):
        pos=0
        while k>=self.split_pos[pos]+self.split_size:
            pos+=1
            if pos==self.split_count-1:
                break
        return pos
    
    def update(self,k,x):
        cur_value=self.table[k]
        self.table[k]=x
        pos=self.get_position(k)
        #--------- update method ---------#
        self.dc[pos][cur_value]-=1
        self.dc[pos][x]+=1
        #--------- update method ---------#
        
    def query(self,l,r,x):
        rt=0
        pos_l=self.get_position(l)
        pos_r=self.get_position(r)
        
        #--------- update method ---------#
        if pos_l==pos_r:
            for i in range(l,r):
                if self.table[i]==x:
                    rt+=1
            return rt
        
        rt=0
        for i in range(pos_l+1,pos_r):
            rt+=self.dc[i][x]
        
        if pos_l<self.split_count-1:
            bound_l=self.split_pos[pos_l+1]
        else:
            bound_l=self.size
        bound_r=self.split_pos[pos_r]
        for i in range(l,bound_l):
            if self.table[i]==x:
                rt+=1
        for i in range(bound_r,r):
            if self.table[i]==x:
                rt+=1
        #--------- update method ---------#
        #show((l,r),x,[pos_l,pos_r],(l,bound_l),[pos_l+1,pos_r-1],(bound_r,r))
        return rt
