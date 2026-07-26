import sys

n, q = map(int, input().split())
a = list(map(int, sys.stdin.readline().strip().split()))

SIZE = (1 << len(a).bit_length())
tree = [(0, 0, 0)] * (2 * SIZE)
tree2 = [0] * (2 * SIZE)

def callback(u, v, r, t):
    return (
        max(u[0], v[0], u[2] + v[1], 0),
        max(u[1], r + v[1], 0),
        max(v[2], u[2] + t, 0))

def make_pair(v):
    return max(v, 0), max(v, 0), max(v, 0)

def build(l, tree):

    N = len(l)
    for i in range(N):
        tree[i + SIZE] = make_pair(l[i])
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = callback(tree[2 * i], tree[2 * i + 1])

def query(l, r, tree):

    l += SIZE
    r += SIZE

    left = make_pair(0)
    right = make_pair(0)

    while l <= r:
        if l & 1:
            left = callback(left, tree[l])
            l += 1
        if r & 1 == 0:
            right = callback(tree[r], right)
            r -= 1
        l >>= 1
        r >>= 1

    return callback(left, right)[0]


def update(x, v, tree):

    x += SIZE
    tree[x] = make_pair(v)
    while x > 1:
        x >>= 1
        tree[x] = callback(tree[2 * x], tree[2 * x + 1])

def build2(l, tree):

    N = len(l)
    for i in range(N):
        tree[i + SIZE] = l[i]
    
    for i in range(SIZE - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]


def update2(x, v, tree):

    x += SIZE
    tree[x] = v
    while x > 1:
        x >>= 1
        tree[x] = callback(tree[2 * x], tree[2 * x + 1])

build(a, tree)

result = []
for line in sys.stdin:
    k, x = map(int, line.split())
    update(k - 1, x, tree)
    result.append(query(0, n - 1, tree))

# print(tree)

print(*result, sep="\n")