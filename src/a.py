import sys
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()
import bisect,string,math,time,functools,random,fractions
from bisect import*
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
rep=range;R=range
def I():return int(input())
def LI():return [int(i) for i in input().split()]
def SLI():return sorted([int(i) for i in input().split()])
def LI_():return [int(i)-1 for i in input().split()]
def S_():return input()
def IS():return input().split()
def LS():return [i for i in input().split()]
def NI(n):return [int(input()) for i in range(n)]
def NI_(n):return [int(input())-1 for i in range(n)]
def NLI(n):return [[int(i) for i in input().split()] for i in range(n)]
def NLI_(n):return [[int(i)-1 for i in input().split()] for i in range(n)]
def StoLI():return [ord(i)-97 for i in input()]
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RLI(n=8,a=1,b=10):return [random.randint(a,b)for i in range(n)]
def RI(a=1,b=10):return random.randint(a,b)
def INP():
    N=6
    n=random.randint(1,N)
    m=random.randint(1,N)
    b=random.randint(1,n)
    w=random.randint(1,m)
    mn=0
    mx=n
    #a=[random.randint(mn,mx) for i in range(n)]
    return n,m,b,w
def Rtest(T):
    case,err=0,0
    for i in range(T):
        inp=INP()
        a1=naive(*inp)
        a2=solve(*inp)
        if a1!=a2:
            print(inp)
            print('naive',a1)
            print('solve',a2)
            err+=1
        case+=1
    print('Tested',case,'case with',err,'errors')
def GI(V,E,ls=None,Directed=False,index=1):
    org_inp=[];g=[[] for i in range(V)]
    FromStdin=True if ls==None else False
    for i in range(E):
        if FromStdin:
            inp=LI()
            org_inp.append(inp)
        else:
            inp=ls[i]
        if len(inp)==2:a,b=inp;c=1
        else:a,b,c=inp
        if index==1:a-=1;b-=1
        aa=a,c,;bb=b,c,;g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp
def RE(E):
    rt=[[]for i in range(len(E))]
    for i in range(len(E)):
        for nb,d in E[i]:
            rt[nb]+=(i,d),
    return rt
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
    #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
    mp=[boundary]*(w+2);found={}
    for i in R(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[boundary]+[mp_def[j] for j in s]+[boundary]
    mp+=[boundary]*(w+2)
    return h+2,w+2,mp,found
def TI(n):return GI(n,n-1)
def accum(ls):
    rt=[0]
    for i in ls:rt+=[rt[-1]+i]
    return rt
def bit_combination(n,base=2):
    rt=[]
    for tb in R(base**n):s=[tb//(base**bt)%base for bt in R(n)];rt+=[s]
    return rt
def gcd(x,y):
    if y==0:return x
    if x%y==0:return y
    while x%y!=0:x,y=y,x%y
    return y
def YN(x):print(['NO','YES'][x])

def Yn(x):print(['No','Yes'][x])
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)

mo=10**9+7
#mo=998244353
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
alp=[chr(ord('a')+i)for i in range(26)]
#sys.setrecursionlimit(10**7)


show_flg=False
show_flg=True

## Segment Tree ##

## Test case: ABC 146 F
## https://atcoder.jp/contests/abc146/tasks/abc146_f

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

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

    def __getitem__(self,key):
        if type(key) is slice:
            a=None if key.start==None else key.start
            b=None if key.stop==None else key.stop
            c=None if key.step==None else key.step
            return self.table[self.num-1:self.num-1+self.size][slice(a,b,c)]
        else:
            if 0<=key<self.size:
                return self.table[key+self.num-1]
            elif -self.size<=key<0:
                return self.table[self.size+key+self.num-1]
            else:
                raise IndexError("list index out of range")

    def __setitem__(self,key,value):
        if key>=0:
            self.update(key,value)
        else:
            self.update(self.size+key,value)

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
ans=0


n,q=LI()
a=LI()
b=LI()

c=[]
d=[]

for i in range(n-1):
    c+=a[i+1]-a[i],
    d+=b[i+1]-b[i],
# Range Minimum:    sg=SegTree(n,inf,min,inf)
#sg1=SparseTable(c,init_func=gcd,init_idl=1)
#sg2=SparseTable(d,init_func=gcd,init_idl=1)
sg1=SegTree(n,0,function=gcd,ide=0)
sg2=SegTree(n,0,function=gcd,ide=0)

for i in range(n-1):
    sg1.update(i,c[i])
    sg2.update(i,d[i])



for i in range(q):
    h1,h2,w1,w2=LI_()
    #show([(i,)],(h1,h2,w1,w2),a[h1:h2+1],b[w1:w2+1])
    if h1<h2:
        g1=sg1.query(h1,h2)
    else:
        g1=a[h1]+b[w1]
    if w1<w2:
        g2=sg2.query(w1,w2)
    else:
        g2=a[h1]+b[w1]
    #g=gcd(a[h1]+b[w1])
    g=a[h1]+b[w1]
    #show((g,g1,g2),(h1,h2,w1,w2))
    ans=gcd(g,gcd(g1,g2))
    if ans<0:ans=-ans
    print(ans)
