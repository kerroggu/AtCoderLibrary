
class accum2d:
    def __init__(self,a):
        h=len(a)
        w=len(a[0])
        self.tbl=[[0]*(w+1)]
        for i in range(h):
            b=[0]
            for c in a[i]:
                b+=b[-1]+c,
            self.tbl+=b,
        for i in range(h):
            for j in range(w+1):
                self.tbl[i+1][j]+=self.tbl[i][j]
    
    def sum(self,a,b,c,d): # return sum of values in [a, b] * [c, d]
        return self.tbl[c+1][d+1]-self.tbl[c+1][b]-self.tbl[a][d+1]+self.tbl[a][b]
        
    def __str__(self):
        return str(self.tbl)
    
    def show(self):
        for i in self.tbl:
            print(i)
