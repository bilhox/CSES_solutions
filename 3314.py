n = int(input())
a = list(map(int, input().split()))

class SegTree:

    def __init__(self, n, callback, neutral):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.callback = callback
        self.array = [neutral] * (2 * self.size)
        self.neutral = neutral

    def range(self, sx, sy):
        return self._range(0, sx, sy, 0, self.size)
    
    def _range(self, x, sx, sy, lx, ly):

        stack = [(x, lx, ly)]
        current_value = self.neutral

        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                current_value = self.callback(current_value, self.array[nx])
                continue

            m = (nlx + nly) // 2

            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 1, nlx, m))
                stack.append((2 * nx + 2, m, nly))
        
        return current_value
    
    def set(self, val, i):
        self._set(val, i, 0, 0, self.size)

    def _set(self, val, i, x, lx, ly):

        stack = [(x, lx, ly, False)]

        while stack:
            nx , nlx, nly, computable = stack.pop()

            if nly - nlx == 1:
                self.array[nx] = val
                continue
            
            if not computable:
                stack.append((nx, nlx, nly, True))
                m = (nlx + nly) // 2

                if i < m:
                    stack.append((2 * nx + 1, nlx, m, False))
                else:
                    stack.append((2 * nx + 2, m, nly, False))
            else:
                self.array[nx] = self.callback(self.array[2 * nx + 1], self.array[2 * nx + 2])

def callback_max_index(u, v):
    if u[0] <= v[0]:
        return v
    else:
        return u

tree = SegTree(n, callback_max_index, (-10**10, 0))
for i in range(n):
    tree.set((a[i], i), i)

stack = [(0, n, 0, None)]
max_so_far = 0
while stack:

    l, r, tot, prev = stack.pop()
    mm, mi = tree.range(l, r)
    
    l1, r1 = l, mi
    l2, r2 = mi + 1, r

    if mm != prev:
        tot += 1

    if r1 - l1 > 0:
        stack.append((l1, r1, tot, mm))
    if r2 - l2 > 0:
        stack.append((l2, r2, tot, mm))
    max_so_far = max(tot, max_so_far)

print(max_so_far)