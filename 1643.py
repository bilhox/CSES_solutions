import math

class SegTree:

    def __init__(self, n : int, values : list[int]):
        self.size = 2**math.ceil(math.log2(n))
        self.values = [0 for _ in range(2 * self.size)]
        print(self.size)
        for i in range(n):
            self.set(values[i], i)
    
    def _set(self, val, i, x, lx, rx):

        if (rx - lx) == 1:
            self.values[x] = val
            return
        m = (lx + rx) // 2
        if i < m:
            self._set(val, i, 2 * x + 1, lx, m)
        else:
            self._set(val, i, 2 * x + 2, m, rx)
        
        self.values[x] = self.values[2 * x + 1] + self.values[2 * x + 2]
    
    def _sum(self, x, sx, sy, lx, rx):
        if rx < sx or lx >= sy:
            return 0
        if sx <= lx and rx <= sy:
            return self.values[x]
        
        m = (lx + rx) // 2

        if sy < m:
            return self._sum(2 * x + 1, sx, sy, lx, m)
        elif sx >= m:
            return self._sum(2 * x + 2, sx, sy, m, rx)
        else:
            return self._sum(2 * x + 1, sx, sy, lx, m) + self._sum(2 * x + 2, sx, sy, m, rx)
    
    def sum(self, sx, sy):
        return self._sum(0, sx, sy, 0, self.size)
    
    def set(self, val, i):
        self._set(val, i, 0, 0, self.size)
    
n = int(input())
a = [int(v) for v in input().split()]
seg = SegTree(n, a)
print(seg.sum(1, 5))