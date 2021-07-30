
class LSG:
    def __init__(self,n, a=None):
        self._n = n
        self._ninf = ninf
        self._op = op
        self._mapping = mapping
        self._composition = composition
        self._f0 = f0
        x = 0
        while (1 << x) < self._n:
            x += 1
        self._log = x
        self._size = 1 << self._log
        self._d = [self._ninf] * (2 * self._size)
        self._lz = [self._f0] * self._size
        if a is not None:
            for i in range(self._n):
                self._d[self._size + i] = a[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    def check(self):
        return [self.query_point(p) for p in range(self._n)]
    def update_point(self, p, x):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    def query_point(self, p):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]
    def query(self, left, right):
        if left == right:
            return self._ninf
        left += self._size
        right += self._size
        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)
        sml = self._ninf
        smr = self._ninf
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1
        return self._op(sml, smr)
    def query_all(self):
        return self._d[1]
    def update(self, left, right, f):
        if right is None:
            p = left
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            if left == right:
                return
            left += self._size
            right += self._size
            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)
            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2
            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)
    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
    def _all_apply(self, k, f) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])
    def _push(self, k):
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._f0
    def loc(self, l, r):
        return self._lz[self._size+l : self._size+r]
    
ninf = 10**9
f0 = 0
def op(x,y):
    return min(x,y)
def mapping(f,x):
    return f+x
def composition(f1,f2):
    return f1+f2
