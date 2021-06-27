## Verified by Yukicoder 1073
## https://yukicoder.me/problems/no/1073
##
## Matrix Class supporting operators +, -, *, %, +=, -=, *=, %=
## *, *= allows int/float/complex
## ** or pow(self,p,mod) for the size N*N matrix is implemented by Repeated squaring. O(N^3*log(p))
##
## Constructor: matrix(array), where array is 1D or 2D array. 1-dimensional array X is modified as 2D array of [X].
##
## methods
## T(): returns transposed matrix
## resize((n,m),fill=0): changes the matrix instance into the new shape (n * m), missing entries are filled with "fill" (default value is zero).


class matrix:
    class MulShapeError(Exception):
        "mult is not applicable between the two matrices given"
        pass

    def __init__(self,arr_input):
        
        if hasattr(arr_input[0],"__getitem__"):
            self.arr=[]
            self.shape=(len(arr_input),len(arr_input[0]))
            for i in arr_input:
                self.arr+=i
        else:
            self.arr=arr_input
            self.shape=(1,len(arr_input))
        

    def __getitem__(self,key):
        return self.arr[key]

    def __setitem__(self,key,value):
        self.arr[key]=value

    def __iter__(self):
        return iter(self.arr)
        
    def __add__(self,B):
        if type(B)!=matrix:
            return NotImplemented
        if B.shape!=self.shape:
            return NotImplemented
        rt=[0]*(self.shape[1]*self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                rt[i*self.shape[1]+j]=self.arr[i*self.shape[1]+j]+B.arr[i*self.shape[1]+j]
        return matrix(rt)

    def __iadd__(self,B):
        return self.__add__(B)

    def __sub__(self,B):
        if type(B)!=matrix:
            return NotImplemented
        if B.shape!=self.shape:
            return NotImplemented
        rt=[0]*(self.shape[1]*self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                rt[i*self.shape[1]+j]=self.arr[i*self.shape[1]+j]-B.arr[i*self.shape[1]+j]
        return matrix(rt)

    def __isub__(self,B):
        return self.__sub__(B)

    def __mul__(self,M,mod=10**9+7):
        if type(M) in [int,float,complex]:
            M=matrix([M*(i==j) for j in range(self.shape[1]) for i in range(self.shape[1])])
            M.resize(self.shape)
        if type(M)!=matrix:
            return NotImplemented
        if M.shape[0]!=self.shape[1]:
            raise matrix.MulShapeError("mult is not applicable between the matrices of shape "+str(self.shape)+" and "+str(M.shape))
        ra,ca=self.shape
        rb,cb=M.shape
        c=[0]*(cb*ra)
        for i in range(ra):
            for j in range(cb):
                for k in range(ca):
                    c[i*cb+j]+=self.arr[i*ca+k]*M.arr[k*cb+j]
                    if c[i*cb+j]>=mod:c[i*cb+j]%=mod
        c=matrix(c)
        c.resize((ra,cb))
        return c
    
    
    def __imul__(self,M):
        return self.__mul__(M)

    def __rmul__(self,M,mod=10**9+7):
        if type(M) in [int,float,complex]:
            M=matrix([M*(i==j) for j in range(self.shape[1]) for i in range(self.shape[1])])
        if type(M)!=matrix:
            return NotImplemented
        if M.shape[0]!=self.shape[1]:
            raise matrix.MulShapeError("mult is not applicable between the matrices of shape "+str(self.shape)+" and "+str(M.shape))
        ra,ca=self.shape
        rb,cb=M.shape
        c=[0]*(cb*ra)
        for i in range(ra):
            for j in range(cb):
                for k in range(ca):
                    c[i*cb+j]+=self.arr[i*ca+k]*M.arr[k*cb+j]
                    if c[i*cb+j]>=mod:c[i*cb+j]%=mod
        c=matrix(c)
        c.resize((ra,cb))
        return c

    def __mod__(self,p):
        if type(p)!=int:
            return NotImplemented
        c=[0]*(self.shape[1]*self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                c[i*self.shape[1]+j]=self.arr[i*self.shape[1]+j]%p
        return matrix(c)

    def __imod__(self,p):
        return self.__mod__(p)

    def __pow__(self,p,mod=10**9+7):
        if type(p)!=int or self.shape[0]!=self.shape[1]:
            return NotImplemented
        A=matrix(self.arr)
        A.resize(self.shape)
        R=matrix([1*(i==j) for j in range(self.shape[0]) for i in range(self.shape[0])])
        R.resize(self.shape)
        while p>0:
            if p&1:
                R*=A
            A*=A
            p>>=1
        return R

    def __neg__(self):
        return self.__mul__(-1)

    def __str__(self):
        rt='['
        for i in range(self.shape[0]):
            row='['
            for j in range(self.shape[1]):
                row=row+str(self.arr[i*self.shape[1]+j])+","
            rt=rt+row[:-1]+"]\n"
        return rt[:-1]+']'

    def T(self):
        rt=[0]*(self.shape[0]*self.shape[1])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                rt[j*self.shape[0]+i]=self.arr[i*self.shape[1]+j]
        rt=matrix(rt)
        rt.resize((self.shape[1],self.shape[0]))
        return rt

    def resize(self,new_shape,fill=0):
        self.shape=new_shape
        if len(self.arr)<self.shape[0]*self.shape[1]:
            self.arr+=[fill]*(self.shape[0]*self.shape[1]-len(self.arr))
        '''t_arr=[]
        for i in self.arr:
            t_arr+=i
        t_arr.reverse()
        n,m=new_shape
        self.shape=(n,m)
        self.arr=[[fill]*m for i in range(n)]

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if t_arr:
                    self.arr[i][j]=t_arr.pop()
        '''
        return

    def view(self):
        for i in self.arr:
            print(i)
