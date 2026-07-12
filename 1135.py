import sys

n, q = map(int, input().split())

tree = [[] for _ in range(n + 1)]
for _, line in zip(range(n - 1), sys.stdin):
    a, b = map(int, line.split())
    tree[a].append(b)
    tree[b].append(a)
    

h = [0] * (2 * n - 1)
start = [-1] * (n + 1)

def dfs():
    ind = 0
    stack = [(-1, 1, 0)]
    for _ in range(2 * n - 1):
        prev, node, height = stack.pop()
        h[ind] = height

        if start[node] == -1:
            start[node] = ind

        ind += 1

        while tree[node]:
            desc = tree[node].pop()
            if desc == prev: continue
            stack.append((prev, node, height))
            stack.append((node, desc, height + 1))
        
        # print(stack)
        # time.sleep(0.1)

dfs()

SIZE = (1 << len(h).bit_length())
segtree = [10**10] * (2 * SIZE)
 
def build(l, tree):
 
    N = len(l)
    for i in range(N):
        tree[i + SIZE] = l[i]
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])
 
def query(l, r, tree):
 
    res = 10**10
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
 
build(h, segtree)
 
# print(segtree)
 
for _, line in zip(range(q), sys.stdin):
    a, b = map(int, line.split())
    
    if start[a] > start[b]:
        a, b = b, a
 
    u = query(start[a], start[b], segtree)
    lca = u

    ha = h[start[a]]
    hb = h[start[b]]

    print(ha + hb - 2 * lca)