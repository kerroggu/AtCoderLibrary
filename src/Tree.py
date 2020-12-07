# Verified by 
# https://atcoder.jp/contests/abc014/tasks/abc014_4
# https://atcoder.jp/contests/abc133/tasks/abc133_f

# import SparseTable
# initialize
# Tree() => n; (a,b);*(n-1)
# Tree(n) => (a,b);*(n-1)
# Tree(init=False); Tree.stdin(); => n; (a,b);*(n-1)
# Tree(init=False); Tree.listin(ls,index=0); => (a,b);*(n-1)

import sys,bisect,string,math,time,functools,random,fractions
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
rep=range
def Golf():n,*t=map(int,open(0).read().split())
def I():return int(input())
def S_():return input()
def IS():return input().split()
def LS():return [i for i in input().split()]
def MI():return map(int,input().split())
def LI():return [int(i) for i in input().split()]
def LI_():return [int(i)-1 for i in input().split()]
def NI(n):return [int(input()) for i in range(n)]
def NI_(n):return [int(input())-1 for i in range(n)]
def StoLI():return [ord(i)-97 for i in input()]
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RA():return map(int,open(0).read().split())
def GI(V,E,ls=None,Directed=False,index=1):
    org_inp=[];g=[[] for i in range(V)]
    FromStdin=True if ls==None else False
    for i in range(E):
        if FromStdin:
            inp=LI()
            org_inp.append(inp)
        else:
            inp=ls[i]
        if len(inp)==2:
            a,b=inp;c=1
        else:
            a,b,c=inp
        if index==1:a-=1;b-=1
        aa=(a,c);bb=(b,c);g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
    #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
    mp=[boundary]*(w+2);found={}
    for i in range(h):
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
    for tb in range(base**n):s=[tb//(base**bt)%base for bt in range(n)];rt+=[s]
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
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**7)
read=sys.stdin.buffer.read
readline=sys.stdin.buffer.readline
input=lambda: sys.stdin.readline().rstrip()

class Tree:
    def __init__(self,inp_size=None,ls=None,init=True,index=1):
        self.LCA_init_stat=False
        self.ETtable=[]
        if init:
            if ls==None:
                self.stdin(inp_size,index=index)
            else:
                self.node_size=len(ls)+1
                self.edges,_=GI(self.node_size,self.node_size-1,ls,index=index)
        return
 
    def stdin(self,inp_size=None,index=1):
        if inp_size==None:
            self.node_size=int(input())
        else:
            self.node_size=inp_size
        self.edges,_=GI(self.node_size,self.node_size-1,index=index)
        return
    
    def listin(self,ls,index=0):
        self.node_size=len(ls)+1
        self.edges,_=GI(self.node_size,self.node_size-1,ls,index=index)
        return
 
    def dfs(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
        return v
 
    def bfs(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        while q:
            c=q.popleft()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
        return v
 
    def parent(self,x):
        return self.dfs(0,func=lambda pr,prv,nx,dist:pr,root_v=-1)
 
    def topological_sort(self,x):  # return topological sort of the tree
        tps=[]
        q=deque([x])
        v=[None]*self.node_size
        v[x]=0
        while q:
            c=q.popleft()
            tps.append(c)
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=0
        return tps
 
    def EulerTour(self,x):
        q=deque()
        q.append(x)
        self.depth=[None]*self.node_size
        self.depth[x]=0
        self.ETtable=[]
        self.ETdepth=[]
        self.ETin=[-1]*self.node_size
        self.ETout=[-1]*self.node_size
        cnt=0
        while q:
            c=q.pop()
            if c<0:
                ce=~c
            else:
                ce=c
                for nb,d in self.edges[ce]:
                    if self.depth[nb]==None:
                        q.append(~ce)
                        q.append(nb)
                        self.depth[nb]=self.depth[ce]+1
            self.ETtable.append(ce)
            self.ETdepth.append(self.depth[ce])
            if self.ETin[ce]==-1:
                self.ETin[ce]=cnt
            else:
                self.ETout[ce]=cnt
            cnt+=1
        return
    
    def doubling_LCA(self,root,x,y):
        if self.LCA_init_stat==False:
            self.depth=[None]*self.node_size
            self.depth=self.bfs(0,func=lambda pr,prv,nxt,dist:prv+1)
            self.par=self.bfs(0,func=lambda pr,prv,nxt,dist:pr)
            self.db=[self.par]
            for i in range(self.node_size.bit_length()):
                #show(self.db)
                self.db+=[[self.db[-1][self.db[-1][i]] for i in range(self.node_size)]]
            self.LCA_init_stat=True
        dx=self.depth[x]
        dy=self.depth[y]
        if dx>dy:
            dx,dy=dy,dx
        c=self.node_size.bit_length()
        while c>0:
            if dx+c<=dy:
                x=self.db[c][x]
                dx+=1<<c
            c>>=1
        
        if x==y:
            return x
        
        c=self.node_size.bit_length()
        while c>0:
            if self.db[c][x]!=self.db[c][y]:
                x=self.db[c][x]
                y=self.db[c][y]
            c>>=1
        
        return self.par[x]
        
    def LCA_init(self,root):
        self.EulerTour(root)
        self.st=SparseTable(self.ETdepth,init_func=min,init_idl=inf)
        #self.st=SegTree(self.node_size*2-1,self.ETdepth,function=min,ide=inf)
        self.LCA_init_stat=True
        return
    
    def LCA(self,root,x,y):
        if self.LCA_init_stat==False:
            self.LCA_init(root)
        xin,xout=self.ETin[x],self.ETout[x]
        yin,yout=self.ETin[y],self.ETout[y]
        a=min(xin,yin)
        b=max(xout,yout,xin,yin)
        id_of_min_dep_in_et=self.st.query_id(a,b+1)
        return self.ETtable[id_of_min_dep_in_et]
 
    def __str__(self):
        return  str(self.edges)
 
    def show(self):
        if all([all([d==1 for nd,d in e]) for e in self.edges]):
            print( [[nd for nd,d in e] for e in self.edges] )
        else:
            print(self)
 
    def dfs2(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        dfs_tr=[x]
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
                    dfs_tr+=nb,
        return v,dfs_tr
