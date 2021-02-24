# Verified by 
# https://atcoder.jp/contests/abc014/tasks/abc014_4
# https://atcoder.jp/contests/abc133/tasks/abc133_f

# import SparseTable
# initialize
# Tree() => n; (a,b);*(n-1)
# Tree(n) => (a,b);*(n-1)
# Tree(init=False); Tree.stdin(); => n; (a,b);*(n-1)
# Tree(init=False); Tree.listin(ls,index=0); => (a,b);*(n-1)

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
 
    def dfs_tour(self,x,root_dep=0):
        q=deque([x])
        dep=[None]*self.node_size
        dep[x]=root_dep
        dfs_tr=[x]
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if dep[nb]==None:
                    q.append(nb)
                    dep[nb]=dep[c]+1
                    dfs_tr+=nb,
        return dep,dfs_tr
