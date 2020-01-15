class Matrix:
    def __init__(self,arr_input):
        self.arr=arr_input

    def __add__(self,B):
        return B.arr
        
    def __str__(self):
        return str(self.arr)

    def mult(self,M):
        a=self.arr
        b=M.arr
        ra,ca=len(a),len(a[0])
        rb,cb=len(b),len(b[0])

        if ca!=rb:
            return None
        c=[[0]*cb for i in range(ra)]
        for i in range(ra):
            for j in range(cb):
                for k in range(ca):
                    c[i][j]+=a[i][k]*b[k][j]
        return Matrix(c)
