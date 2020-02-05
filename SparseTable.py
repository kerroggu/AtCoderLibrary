class SparseTable: # O(N log N) for init, O(1) for query(l,r)
    def __init__(self,ls,init_func=min,init_idl=float('inf')):
        self.func=init_func
        self.idl=init_idl
        self.size=len(ls)
        self.N0=self.size.bit_length()
        self.table=[ls[:]]

        for i in range(self.N0):
            tmp=[self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) for j in range(self.size)]
            self.table+=[tmp]
    
    # return func of [l,r)
    def query(self,l,r):
        N=(r-l).bit_length()-1
        return self.func(self.table[N][l],self.table[N][r-(1<<N)])
    
    def print(self):
        for i in self.table:
            print(*i)
