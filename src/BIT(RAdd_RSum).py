# Range add, Range sum BIT
# from https://tjkendev.github.io/procon-library/python/range_query/rsq_ruq_segment_tree_lp.html
# Validated by ABC253 F https://atcoder.jp/contests/abc253/tasks/abc253_f

class Bit:
    def __init__(self, N):
        # N: 処理する区間の長さ
        self.N=N
        self.data0 = [0]*(self.N+1)
        self.data1 = [0]*(self.N+1)
    
    # 区間[l, r)に x を加算
    def _add(self, data, k, x):
        while k <= self.N:
            data[k] += x
            k += k & -k
    def add(self, l, r, x):
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)
    
    # 区間[l, r)の和を求める
    def _get(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        
        return s
    def query(self, l, r):
        return self._get(self.data1, r-1) * (r-1) + self._get(self.data0, r-1) - self._get(self.data1, l-1) * (l-1) - self._get(self.data0, l-1)

    # return list for debug
    def show(self):
        r=[0]*(self.N+1)
        for i in range(1,self.N+1*0):
            r[i]=self.query(i,i+1)
        return r


class Bit0(Bit): # 0-indexed
    def add(self,l,r,x):
        super().add(l+1,r+1,x)
    def query(self,l,r):
        return super().query(l+1,r+1)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)
    def u_bound(self,w):
        return max(super().u_bound(w)-1,0)

def compress(L):
    dc={v:i for i,v in enumerate(sorted(set(L)))}
    return [dc[i] for i in L]
