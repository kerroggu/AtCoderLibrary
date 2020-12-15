# Verified by AGC033 A
# https://atcoder.jp/contests/agc033/tasks/agc033_a

class Graph:
    def __init__(self,inp_node_size=None,inp_edge_size=None,ls=None,init=True,Directed=False,index=1):
        if init:
            self.IsGrid=False
            if ls==None:
                self.stdin(inp_node_size,inp_edge_size,Directed=Directed,index=index)
            else:
                self.listin(ls,Directed=Directed,index=index)
        else:
            self.edges=[]
        return
 
    def stdin(self,inp_node_size=None,inp_edge_size=None,Directed=False,index=1):
        if (inp_node_size,inp_edge_size)==(None,None):
            self.node_size,self.edge_size=LI()
            self.edges,_=GI(self.node_size,self.edge_size,Directed=Directed,index=index)
        else:
            self.node_size,self.edge_size=inp_node_size,inp_edge_size
            self.edges,_=GI(self.node_size,self.edge_size,Directed=Directed,index=index)
        return
 
    def listin(self,inp_node_size,ls,Directed=False,index=0):
        self.node_size,self.edge_size=inp_node_size,len(ls)
        self.edges,_=GI(self.node_size,self.edge_size,ls,Directed=Directed,index=index)
        return
 
    def edgein(self,inp_edge,index=0):
        self.node_size,self.edge_size=len(inp_edge),0
        self.edges=[0]*self.node_size
        for i in range(self.node_size):
            self.edges[i]=inp_edge[i][:]
        return
 
    def gridin(self,h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0}):
        #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
        self.mp,found=[],{}
        if search==None:
            search=[]
        self.node_size,self.edge_size,self.grid_h,self.grid_w=h*w,0,h,w
        self.edges=[[] for i in range(self.node_size)]
        self.IsGrid=True
        for i in range(h):
            s=input()
            for char in search:
                if char in s:
                    found[char]=(i*w+s.index(char))
                    mp_def[char]=mp_def[replacement_of_found]
            for j in s:
                self.mp.append(mp_def[j])
        for dd in [1,w]:
            r_end=0
            for node in range(self.node_size):
                r_end+=1
                if r_end==w:
                    r_end=0
                nx=node+dd
                if nx<0 or self.node_size<=nx or (dd==1 and r_end==0):
                    continue
                if self.mp[nx]==0:
                    self.edges[node].append(nx)
                if self.mp[node]==0:
                    self.edges[nx].append(node)
        return found
 
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
        q=deque([i for i,j in enumerate(self.mp) if j==1])
        v=[None]*self.node_size
        #v[x]=root_v
        for y in q:v[y]=root_v
        while q:
            c=q.popleft()
            for nb in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=v[c]+1
        return v
 
    def parent(self,x):
        return self.bfs(0,func=lambda pr,prv,nx,dist:pr,root_v=-1)
 
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
 
    def dijkstra(self,st):
        # edge=[[(v_to,dist_to_v),...],[],...]
        # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
        d=[(0 if st==i else inf) for i in range(self.node_size)]
        prev=[0]*self.node_size
        q=[(j,i) for i,j in enumerate(d)]
        heapify(q)
        v=[False]*self.node_size
        # calc
        while q:
            dist,cur=heappop(q)
            if v[cur]:
                continue
            v[cur]=True
            for dst,dist in self.edges[cur]:
                alt=d[cur]+dist
                if alt<d[dst]:
                    d[dst]=alt
                    prev[dst]=cur
                    heappush(q,(alt,dst))
        return d,prev
    
    def __str__(self):
        if self.IsGrid:
            for i in range(self.grid_h):
                print(*self.mp[i*self.grid_w:-~i*self.grid_w])
            return str(str(self.show()))
        else:
            return  str(str(self.show()))
 
    def show(self):  # hide distance when all distance == 1
        if self.IsGrid:
            rt=[[nd for nd,d in e] for e in self.edges]
            return 'Grid',rt
        else:
            if all([all([d==1 for nd,d in e]) for e in self.edges]):
                rt=[[nd for nd,d in e] for e in self.edges]
                return 'Simplified',rt
            else:
                return self
 
