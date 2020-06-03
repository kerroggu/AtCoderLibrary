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
                self.size=len(ls)+1
                self.edges,_=GI(self.size,self.size-1,ls,index=index)
        return
 
    def stdin(self,inp_size=None,index=1):
        if inp_size==None:
            self.size=int(input())
        else:
            self.size=inp_size
        self.edges,_=GI(self.size,self.size-1,index=index)
        return
    
    def listin(self,ls,index=0):
        self.size=len(ls)+1
        self.edges,_=GI(self.size,self.size-1,ls,index=index)
        return

    def dfs(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.size
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
        v=[None]*self.size
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
        v=[None]*self.size
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
        self.depth=[None]*self.size
        self.depth[x]=0
        self.ETtable=[]
        self.ETdepth=[]
        self.ETin=[-1]*self.size
        self.ETout=[-1]*self.size
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
    
    def LCA_init(self,root):
        self.EulerTour(root)
        self.st=SparseTable(self.ETdepth,init_func=min,init_idl=inf)
        #self.st=SegTree(self.size*2-1,self.ETdepth,function=min,ide=inf)
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
        if all([all([d==1 for nd,d in edge]) for edge in self.edges]):
            print( [[nd for nd,d in edge] for edge in self.edges] )
        else:
            print(self)
