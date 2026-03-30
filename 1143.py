
class SegTree:

    def __init__(self, A, callback, neutral):
        self.size = 1
        while self.size < len(A):
            self.size *= 2
        
        self.callback = callback
        self.array = [neutral] * (2 * self.size)
        self.neutral = neutral
        self.A = A
    
    def find(self, v):
        return self._find(v)
    
    def _find(self, v):
        
        x = 0
        current = self.array[0]
        if self.A[current] < v:
            return 0
        
        while x < self.size - 1:

            a = self.array[2 * x + 1]
            b = self.array[2 * x + 2]

            if self.A[a] < v and self.A[b] < v:
                return current
            
            if self.A[a] >= v:
                current = a
                x = 2 * x + 1
                continue

            if self.A[b] >= v:
                current = b
                x = 2 * x + 2
                continue
        
        return current

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

n, m = map(int, input().split())
A = [-10**12] + list(map(int, input().split()))

def callback_maxi(u, v):
    if A[u] < A[v]:
        return v
    else:
        return u

callback_min = min
callback_max = max
callback_sum = lambda u, v : u + v
callback_xor = lambda u, v : u ^ v


tree = SegTree(A, callback_maxi, 0)

for i in range(n + 1):
    tree.set(i, i)

queries = list(map(int, input().split()))
result = []
for k in queries:
    i = tree.find(k)
    result.append(i)
    if i != 0:
        A[i] -= k
        tree.set(i, i)

print(*result)
