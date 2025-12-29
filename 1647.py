import math
from itertools import accumulate

class SegTree:

    def __init__(self, n):
        self.size = 1
        while self.size < n: 
            self.size *= 2
        self.values = [math.inf for _ in range(2 * self.size)]
    
    def _set(self, v, i, x, lx, ly):
        if ly - lx == 1:
            self.values[x] = v
            return
        
        m = (lx + ly) // 2

        if i < m:
            self._set(v, i, 2 * x + 1, lx, m)
        else:
            self._set(v, i, 2 * x + 2, m, ly)
        
        self.values[x] = min(self.values[2 * x + 1], self.values[2 * x + 2])
    
    def set_val(self, v, i):
        self._set(v, i, 0, 0, self.size)
    
    def _min(self, x, sx, sy, lx, rx):
        if rx < sx or sy <= lx:
            return math.inf
        
        if sx <= lx <= rx <= sy:
            return self.values[x]
        
        m = (lx + rx) // 2
        if sy < m:
            return self._min(2 * x + 1, sx, sy, lx, m)
        elif sx >= m:
            return self._min(2 * x + 2, sx, sy, m, rx)
        else:
            return min(self._min(2 * x + 1, sx, sy, lx, m), self._min(2 * x + 2, sx, sy, m, rx))
    
    def get_min(self, l, r):
        return self._min(0, l, r, 0, self.size)

n, q = map(int, input().split())
a = list(map(int, input().split()))
tree = SegTree(n)
for i in range(n):
    tree.set_val(a[i], i)
# lookup = []
# log = math.ceil(math.log2(n))
# if n < 2**log:
#     a += [math.inf for _ in range(2**log - n)]
# lookup.append(a)
# for i in range(1, log + 1):
#     line = []
#     prev = lookup[-1]
#     for j in range(0, len(prev), 2):
#         line.append(min(prev[j], prev[j + 1]))
#     lookup.append(line)


# def constitute_minimum(lookup, l, r, k):
#     stage = int(math.log2(k))
#     if r < l:
#         return math.inf
#     elif r - l == 0:
#         return lookup[0][l]
#     elif l % k == 0 and r % k == 0:
#         return constitute_minimum(lookup, l, r, 2 * k)
#     elif l % k == 0:
#         dr = r % k
#         r_bis = r - dr
#         return min(lookup[stage - 1][r // 2**(stage - 1)], constitute_minimum(lookup, l, r_bis, 2*k))
#     elif r % k == 0:
#         dl = k - r % k
#         l_bis = l + dl
#         return min(lookup[stage - 1][l // 2**(stage - 1)], constitute_minimum(lookup, l_bis, r, 2*k))
#     else:
#         dr = r % k
#         r_bis = r - dr
#         dl = k - r % k
#         l_bis = l + dl

#         res1 = constitute_minimum(lookup, l, r_bis, 2*k)
#         res2 = constitute_minimum(lookup, l_bis, r, 2*k)
#         res3 = lookup[stage - 1][r // 2**(stage - 1)]
#         res4 = lookup[stage - 1][l // 2**(stage - 1)]
#         return min(res1, res2, res3, res4)

for _ in range(q):
    l, r = map(int, input().split())
    print(tree.get_min(l - 1, r))