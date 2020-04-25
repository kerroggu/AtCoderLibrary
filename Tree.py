class Tree:
    def __init__(self,init=True):
        if init:
            self.stdin()
        return

    def stdin(self,inp_size=None):
        if inp_size==None:
            self.size=int(input())
        else:
            self.size=inp_size
        self.edges,_=GI(self.size,self.size-1)
        return
    
    def listin(self,ls):
        self.size=len(ls)+1
        self.edges=[[]for i in range(self.size)]
        for a,b in ls:
            self.edges[a].append(b)
            self.edges[b].append(a)
        return

    def __str__(self):
        return  str(self.edges)

    def dfs(self,x,func=lambda x:x+1,root_v=0):
        q=deque()
        q.append(x)
        v=[-1]*self.size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb in self.edges[c]:
                if v[nb]==-1:
                    q.append(nb)
                    v[nb]=func(v[c])
        return v

    def EulerTour(self,x,func=lambda x:x+1,root_v=0):
        q=deque()
        q.append((-1,x))
        v=[None]*self.size
        v[x]=root_v
        et=[]
        while q:
            cb,ce=q.pop()
            et.append(ce)
            for nb in self.edges[ce]:
                if v[nb]==None:
                    q.append((nb,ce))
                    q.append((ce,nb))
                    v[nb]=func(v[ce])
        vid=[[-1,-1]for i in range(self.size)]
        for i,j in enumerate(et):
            if vid[j][0]==-1:
                vid[j][0]=i
            else:
                vid[j][1]=i
        return v,et,vid
    
    def LCA_init(self,depth,et):
        self.st=SegTree(self.size*2-1,func=min,ide=inf)
        for i,j in enumerate(et):
            self.st.update(i,j)
        self.LCA_init_stat==True
        return
    
    def LCA(self,root,x,y):
        if self.LCA_init_stat==False:
            depth,et,vid=self.EulerTour(root)
            self.LCA_init(depth,et)
        return self.st.query(x,y+1)
