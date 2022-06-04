## Tested by ABC254-F
## https://atcoder.jp/contests/abc254/tasks/abc254_f
## Tested by EduFor 88 D
## https://codeforces.com/contest/1359/problem/D

## Init with min: SparseTable(list_a,init_func=min)
## Init with gcd: SparseTable(list_a,init_func=gcd)

class SparseTable: # O(N log N) for init, O(1) for query(l,r)
    def __init__(self,ls,init_func=min):
        self.func=init_func
        self.size=len(ls)
        self.N0=self.size.bit_length()
        self.table=[ls[:]]
        self.index=[list(range(self.size))]
        self.lg=[0]*(self.size+1)
        
        for i in range(2,self.size+1):
            self.lg[i]=self.lg[i>>1]+1
 
        for i in range(self.N0):
            tmp=[self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) for j in range(self.size)]
            tmp_id=[self.index[i][j] if self.table[i][j]==self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) else self.index[i][min(j+(1<<i),self.size-1)] for j in range(self.size)]
            self.table+=[tmp]
            self.index+=[tmp_id]
    
    # return func of [l,r)
    def query(self,l,r):
        if r>self.size:r=self.size
        #N=(r-l).bit_length()-1
        N=self.lg[r-l]
        return self.func(self.table[N][l],self.table[N][max(0,r-(1<<N))])
    
    # return index of which val[i] = func of v among [l,r)
    def query_id(self,l,r):
        if r>self.size:r=self.size
        #N=(r-l).bit_length()-1
        N=self.lg[r-l]
        a,b=self.index[N][l],self.index[N][max(0,r-(1<<N))]
        if self.table[0][a]==self.func(self.table[N][l],self.table[N][max(0,r-(1<<N))]):
            b=a
        return b
    
    # return boundary index of r such that func({table[i]} =< x , i in [pos,r]
    def right_bound(self,pos,x):
        k=(self.size-pos).bit_length()
        for j in range(k)[::-1]:
            nx=pos+(1<<j)
            if nx<n and self.query(pos,nx+1)<=x:
                pos+=(1<<j)
        return pos
    
    # return boundary index of l such that func({table[i]} =< x , i in [l,pos]
    def left_bound(self,pos,x):
        k=pos.bit_length()
        for j in range(k)[::-1]:
            nx=pos-(1<<j)
            if 0<=nx and self.query(nx,pos+1)<=x:
                pos-=(1<<j)
        return pos

    def __str__(self):
        return str(self.table[0])
 
    def print(self):
        for i in self.table:
            print(*i)
