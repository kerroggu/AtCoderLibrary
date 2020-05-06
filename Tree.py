# import SparseTable
# initialize
# Tree() => n; (a,b);*(n-1)
# Tree(n) => (a,b);*(n-1)
# Tree(init=False); Tree.stdin(); => n; (a,b);*(n-1)
# Tree(init=False); Tree.listin(); => (a,b);*(n-1)

class Tree:
    def __init__(self,inp_size=None,init=True):
        self.LCA_init_stat=False
        self.ETtable=[]
        if init:
            self.stdin(inp_size)
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

    def __str__(self):
        return  str(self.edges)

    def dfs(self,x,func=lambda prv,nx,dist:prv+dist,root_v=0):
        q=deque()
        q.append(x)
        v=[-1]*self.size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==-1:
                    q.append(nb)
                    v[nb]=func(v[c],nb,d)
        return v

    def EulerTour(self,x,func=lambda prv,nx,dist:prv+1,root_v=0):
        q=deque()
        q.append(x)
        depth=[None]*self.size
        depth[x]=root_v
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
                    if depth[nb]==None:
                        q.append(~ce)
                        q.append(nb)
                        depth[nb]=depth[ce]+1
            self.ETtable.append(ce)
            self.ETdepth.append(depth[ce])
            if self.ETin[ce]==-1:
                self.ETin[ce]=cnt
            else:
                self.ETout[ce]=cnt
            cnt+=1
        return depth
    
    def LCA_init(self,root):
        self.EulerTour(root,func=lambda prv,nx,dist:prv+dist,root_v=0)
        self.st=SparseTable(self.ETdepth,init_func=min,init_idl=inf)
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
