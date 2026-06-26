
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
        csum = 0
        while x < self.size - 1:

            a = self.array[2 * x + 1]

            if csum + a < v:
                csum += a 
                x = 2 * x + 2
            else:
                x = 2 * x + 1
        
        return x - self.size + 1

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

n = int(input())
A = list(map(int, input().split()))

callback_min = min
callback_max = max
callback_sum = lambda u, v : u + v
callback_xor = lambda u, v : u ^ v
callback_sumsup = lambda u, v : (u >= 0) + (v >= 0)

tree = SegTree(A, callback_sum, 0)

for i in range(n):
    tree.set(1, i)

queries = list(map(int, input().split()))
result = []
for k in queries:
    i = tree.find(k)
    result.append(A[i])
    tree.set(0, i)

print(*result)
