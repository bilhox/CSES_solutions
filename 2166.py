import sys
from collections import deque
class SegTree:

    def __init__(self, n, callback, neutral):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.op = callback
        self.array = [neutral] * (2 * self.size)
        self.neutral = neutral

    def build(self, array):

        for i in range(len(array)):
            self.array[self.size - 1 + i] = (max(0, array[i]), min(0, array[i]))

        for i in range(self.size - 2, -1, -1):
            self.array[i] = self.op(self.array[2 * i + 1], self.array[2 * i + 2])

    def query(self, sx, sy):
        stack = [(0, 0, self.size)]
        current_value = self.neutral

        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                current_value = self.op(current_value, self.array[nx])
                # print(current_value, self.array[nx])
                continue

            m = (nlx + nly) // 2

            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 2, m, nly))
                stack.append((2 * nx + 1, nlx, m))
        
        return current_value
    
    def update(self, val, i):
        stack = [(0, 0, self.size, False)]

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
                self.array[nx] = self.op(self.array[2 * nx + 1], self.array[2 * nx + 2])

def callback(u, v):
    if u[0] + u[1] + v[0] > u[0]:
        return (u[0] + u[1] + v[0], v[1])
    else:
        return (u[0], u[1] + v[0] + v[1])

n, q = map(int, input().split())
a = list(map(int, sys.stdin.readline().strip().split()))

SIZE = (1 << len(a).bit_length())
tree = [(0, 0)] * (2 * SIZE)

def build(l, tree):

    N = len(l)
    for i in range(N):
        tree[i + SIZE] = max(l[i], 0), min(l[i], 0)
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = callback(tree[2 * i], tree[2 * i + 1])

def query(l, r, tree):

    l += SIZE
    r += SIZE

    left = (0, 0)
    right = (0, 0)

    while l <= r:
        if l & 1:
            left = callback(left, tree[l])
            l += 1
        if r & 1 == 0:
            right = callback(tree[r], right)
            r -= 1
        l >>= 1
        r >>= 1

    result = callback(left, right)

    return result[0]


def update(x, v, tree):

    x += SIZE
    tree[x] = max(0, v), min(0, v)
    while x > 1:
        x >>= 1
        tree[x] = callback(tree[2 * x], tree[2 * x + 1])

build(a, tree)

# print(tree.array)

result = []
for line in sys.stdin:
    u, v, w = map(int, line.split())
    if u == 1:
        update(v - 1, w, tree)
        #print(tree)
    else:
        result.append(query(v - 1, w - 1, tree))

print(*result, sep="\n")