class seg():
    # N: 処理する区間の長さ
    def __init__(self,n):
        N = n
        
        inf = 2**31-1
        
        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    def get_table(self):
        return self.data[2**sg.LV-1:2**sg.LV-1+n]
        
    def __str__(self):
        return str(self.data[2**sg.LV-1:2**sg.LV-1+n])
        
    def gindex(self, l, r):
        L = (l + self.N0) >> 1; R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1
    
    # 遅延伝搬処理
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0
    
    # 区間[l, r)にxを加算
    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
    
        L = self.N0 + l; R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x; self.data[R-1] += x
            if L & 1:
                self.lazy[L-1] += x; self.data[L-1] += x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i])
    
    # 区間[l, r)内の最小値を求める
    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l; R = self.N0 + r
    
        s = inf
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
