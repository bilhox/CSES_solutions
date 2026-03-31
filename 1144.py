import sys

class SegTree:

    def __init__(self, n, callback, neutral):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.callback = callback
        self.array = [neutral] * (2 * self.size)
        self.neutral = neutral

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
                self.array[nx] = self.callback(self.array[2 * nx + 1], self.array[2 * nx + 2])

def callback_interval(u, v):
    return [min(u[0], v[0]), max(u[1], v[1]), u[2] + v[2]]



n, q = list(map(int, input().split()))

callback_min = min
callback_max = max
callback_sum = lambda u, v : u + v
callback_xor = lambda u, v : u ^ v
callback_sumsup = lambda u, v : (u >= 0) + (v >= 0)

tree = SegTree(n, callback_interval, (10**10, -10**10, 0))

i = 0
for r in (int(u) for u in sys.stdin.readline().split()):
    tree.set([r, r, 1], i)
    i += 1

result = []
for _ in range(q):
    s, a, b =  input().split()
    a = int(a)
    b = int(b)
    if s == "!":
        tree.set([b, b, 1], a - 1)
    else:
        result.append(str(tree.query(a, b)))

print("\n".join(result))
