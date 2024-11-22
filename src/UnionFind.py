## Tested by ABC264-E
## https://atcoder.jp/contests/abc264/tasks/abc264_e
## Tested by ABC120-D
## https://atcoder.jp/contests/abc120/tasks/abc120_d

class UnionFind:
    def __init__(self,n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.parent=[-1]*n
        # 連結成分の個数を管理
        self._size=[1]*n
        # 何か管理するデータを追加する時 self._left=list(range(n))
 
    def root(self,x):
        if self.parent[x]<0:
            return x
        else:
            # 経路の圧縮
            # 何か管理するデータを追加する時 self._left[self.parent[x]]=min(self._left[self.parent[x]],self._left[self.parent[x]])
            self.parent[x]=self.root(self.parent[x])
            # 何か管理するデータを追加する時 self._left[self.parent[x]]=min(self._left[self.parent[x]],self._left[self.parent[x]])
            return self.parent[x]
 
    def same(self,x,y):
        return self.root(x)==self.root(y)
 
    def union(self,x,y):
        r1=self.root(x)
        r2=self.root(y)
        if r1==r2:
            return
        # ランクの取得
        d1=self.parent[r1]
        d2=self.parent[r2]
        if d1<=d2:
            self.parent[r2]=r1
            self._size[r1]+=self._size[r2]
            if d1==d2:
                self.parent[r1]-=1
        else:
            self.parent[r1]=r2
            self._size[r2]+=self._size[r1]
        # 何か管理するデータを追加する時 rootを取ると経路圧縮が起こるのでr1,r2を使って更新する
        # 何か管理するデータを追加する時 self._left[r1]=min(self._left[r1],self._left[r2])
        # 何か管理するデータを追加する時 self._left[r2]=min(self._left[r1],self._left[r2])

    def size(self,x):
        return self._size[self.root(x)]
        
    def __str__(self):
        rt=[i if j<0 else j for i,j in enumerate(self.parent)]
        return str(rt)
