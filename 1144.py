import sys
import time
 
class SegTree:
 
    def __init__(self, A, callback, neutral):
        self.size = 1
        while self.size < len(A):
            self.size *= 2
        
        self.callback = callback
        self.array = [neutral.copy() for _ in range(2 * self.size)]
        self.neutral = neutral
        self.A = A
 
    def query(self, a, b):
 
        stack = [0]
        result = 0
 
        while stack:
            nx = stack.pop()
 
            u = self.array[2 * nx + 1]
            v = self.array[2 * nx + 2]
            if a <= u[0] <= u[1] <= b:
                result += u[2]
            elif u[1] >= a and u[0] <= b:
                stack.append(2 * nx + 1)
            
            if a <= v[0] <= v[1] <= b:
                result += v[2]
            elif v[1] >= a and v[0] <= b:
                stack.append(2 * nx + 2)
        
        return result
    
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
                self.callback(self.array[nx], self.array[2 * nx + 1], self.array[2 * nx + 2])
 
def callback_interval(w, u, v):
    w[0] = min(u[0], v[0])
    w[1] = max(u[1], v[1])
    w[2] = u[2] + v[2]
 
inp = iter(sys.stdin.readlines())
 
n, q = map(int, next(inp).split())
A = list(map(int, next(inp).split()))
 
callback_min = min
callback_max = max
callback_sum = lambda u, v : u + v
callback_xor = lambda u, v : u ^ v
callback_sumsup = lambda u, v : (u >= 0) + (v >= 0)
 
tree = SegTree(A, callback_interval, [10**10, 0, 0])
 
for i in range(n):
    tree.set([A[i], A[i], 1], i)
 
result = []
u = time.time()
for q in range(q):
    s, a, b = next(inp).split()
    if s == "!":
        tree.set([int(b), int(b), 1], int(a) - 1)
    else:
        result.append(tree.query(int(a), int(b)))
    if time.time() - u > 0.5:
        print(q)
        u = time.time()
 
for v in result:
    print(v)