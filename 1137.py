import sys

n, q = map(int, input().split())
v = list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]

for i, line in zip(range(n - 1), sys.stdin):
    a, b = map(int, line.split())
    tree[a].append(b)
    tree[b].append(a)

start = [0] * (n + 1)
end = [-1] * (n + 1)
timer = 0
stack = [(-1, 1)]
 
while stack:
    prev, node = stack.pop()
 
    if end[node] == 0:
        end[node] = timer
        continue
 
    timer += 1
    start[node] = timer
 
    if end[node] == -1:
        stack.append((prev, node))
        end[node] = 0
    
    for desc in tree[node]:
        if desc == prev: continue
        stack.append((node, desc))

u = [0] * (n + 1)
for i in range(1, n + 1):
    u[start[i]] = v[i - 1]

SIZE = (1 << len(u).bit_length())
segtree = [0] * (2 * SIZE)

def build(l, tree):

    N = len(l)
    for i in range(N):
        tree[i + SIZE] = l[i]
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

def query(l, r, tree):

    res = 0
    l += SIZE
    r += SIZE

    while l <= r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1 == 0:
            res += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    
    return res


def update(x, v, tree):

    x += SIZE
    tree[x] = v
    while x > 1:
        x >>= 1
        tree[x] = tree[2 * x] + tree[2 * x + 1]

build(u, segtree)

for _, line in zip(range(q), sys.stdin):
    quer = list(map(int, line.split()))
    if quer[0] == 1:
        update(start[quer[1]], quer[2], segtree)
    else:
        print(query(start[quer[1]], end[quer[1]], segtree))