class SparseTable: # O(N log N) for init, O(1) for query(l,r)
    def __init__(self,ls,init_func=min,init_idl=float('inf')):
        self.func=init_func
        self.idl=init_idl
        self.size=len(ls)
        self.N0=self.size.bit_length()
        self.table=[ls[:]]
        self.index=[list(range(self.size))]

        for i in range(self.N0):
            tmp=[self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) for j in range(self.size)]
            tmp_id=[self.index[i][j] if self.table[i][j]==self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) else self.index[i][min(j+(1<<i),self.size-1)] for j in range(self.size)]
            self.table+=[tmp]
            self.index+=[tmp_id]
    
    # return func of [l,r)
    def query(self,l,r):
        N=(r-l).bit_length()-1
        return self.func(self.table[N][l],self.table[N][r-(1<<N)])
    
    # return index of which val[i] = func of v among [l,r)
    def query_id(self,l,r):
        N=(r-l).bit_length()-1
        a,b=self.index[N][l],self.index[N][r-(1<<N)]
        if self.table[0][a]==self.func(self.table[N][l],self.table[N][r-(1<<N)]):
            b=a
        return b
    
    def __str__(self):
        return str(self.table[0])
        
    def print(self):
        for i in self.table:
            print(*i)
