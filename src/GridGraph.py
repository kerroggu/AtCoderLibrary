# verified by https://atcoder.jp/contests/abc176/tasks/abc176_d
# verified by https://atcoder.jp/contests/atc001/tasks/dfs_a

# Sample usage
# __init__(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1)
#

class GridGraph:
    def __init__(self,h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
        self.h=h+2
        self.w=w+2
        self.size=self.h*self.w
        self.edges=[[]for i in range(self.size)]
        self.nb=[-1,1,-self.w,self.w]
        self.mp=[boundary]*self.w
        self.found={}
        for i in range(self.h-2):
            s=input()
            self.mp+=[boundary]
            for j in range(self.w-2):
                char=s[j]
                if search and char in search:
                    self.found[char]=((i+1)*self.w+j+1)
                    mp_def[char]=mp_def[replacement_of_found]
                self.mp+=[mp_def[char]]
            self.mp+=[boundary]
        self.mp+=[boundary]*self.w
        return
    
    def coordinate_to_2D(x):return x//self.w,x%self.w
    def coordinate_to_1D(r,c):return r*self.w+c
        
    def __getitem__(self,key):
        return gg.mp[key*self.w:(key+1)*self.w]

    def create_edge(self,cost_func=lambda x,y:1):
        for i in range(self.size):
            if self.mp[i]==1:
                continue
            for di in self.nb:
                nx=i+di
                if self.mp[nx]!=1:
                    self.edges[i].append((nx,cost_func(self.mp[i],self.mp[nx])))
        return self.edges

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

    def __str__(self):
        for i in range(self.h):
            print(self.mp[i*self.w:(i+1)*self.w])
        return ''
 
    def show_node_num(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in range(i*self.w,(i+1)*self.w)])

    def show_map(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in self.mp[i*self.w:(i+1)*self.w]])

    def show_map_w_node_num(self,length=2):
        for i in range(self.h):
            print(*[[' '*(length-(len(str(j))))+str(j),self.mp[j]] for j in range(i*self.w,(i+1)*self.w)])
    
    def show_edges(self,length=2):
        for i in range(self.h):
            print(*[(j,self.edges[j]) for j in range(i*self.w,(i+1)*self.w) if self.edges[j]])
