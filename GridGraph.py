# Under construction
# To be verified by https://atcoder.jp/contests/abc176/tasks/abc176_d

class GridGraph:
    def __init__(self,h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
        self.h=h+2
        self.w=w+2
        self.nb=[-1,1,-w,w]
        #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
        self.mp=[boundary]*self.w
        self.found={}
        for i in range(self.h-2):
            s=input()
            self.mp+=[boundary]
            for i in range(self.w-2):
                char=s[i]
                if search and char in search:
                    self.found[char]=((i+1)*self.w+i+1)
                    mp_def[char]=mp_def[replacement_of_found]
                self.mp+=[mp_def[char]]
            self.mp+=[boundary]
        self.mp+=[boundary]*self.w
        self.h,self.w,self.mp,self.found
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

    def __str__(self):
        for i in range(self.h):
            print(self.mp[i*self.w:(i+1)*self.w])
        return ''
 
    def show_map(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in self.mp[i*self.w:(i+1)*self.w]])

    def show_node_num(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in range(i*self.w,(i+1)*self.w)])

    def show_map_w_node_num(self,length=2):
        for i in range(self.h):
            print(*[[' '*(length-(len(str(j))))+str(j),self.mp[j]] for j in range(i*self.w,(i+1)*self.w)])

        
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
