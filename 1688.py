import sys
import time

X = 2637163838461

n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [set() for _ in range(n + 1)]
for i in range(n - 1):
    tree[a[i]].add((i + 2) ^ X)

tour = [0] * (2 * n - 1)
h = [0] * (2 * n - 1)
start = [-1] * (n + 1)

def dfs():
    ind = 0
    stack = [(1, 0)]
    for _ in range(2 * n - 1):
        node, height = stack.pop()
        tour[ind] = node
        h[ind] = height

        if start[node] == -1:
            start[node] = ind

        ind += 1

        cand = None

        for desc in tree[node]:
            stack.append((node, height))
            stack.append((desc ^ X, height + 1))
            cand = desc
            break
        
        tree[node].discard(cand)
        
        # print(stack)
        # time.sleep(0.1)

dfs()

SIZE = (1 << len(tour).bit_length())
segtree = [(10**10, 0)] * (2 * SIZE)
 
def build(l, tree):
 
    N = len(l)
    for i in range(N):
        tree[i + SIZE] = l[i]
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])
 
def query(l, r, tree):
 
    res = (10**10, 0)
    l += SIZE
    r += SIZE
 
    while l <= r:
        if l & 1:
            res = min(res, tree[l])
            l += 1
        if r & 1 == 0:
            res = min(res, tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    
    return res
 
 
def update(x, v, tree):
 
    x += SIZE
    tree[x] = v
    while x > 1:
        x >>= 1
        tree[x] = min(tree[2 * x], tree[2 * x + 1])
 
build(list(zip(h, tour)), segtree)
 
# print(segtree)
 
for _, line in zip(range(q), sys.stdin):
    a, b = map(int, line.split())
    
    if start[a] > start[b]:
        a, b = b, a
 
    u = query(start[a], start[b], segtree)
    print(u[1])