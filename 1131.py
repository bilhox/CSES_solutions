from collections import deque
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

leaf = [0] * N
max_length = [0] * N

def dfs(s):

    stack = [(-1, s, 0)]
    dist = [0] * (N + 1)
    path = {}

    while stack:
        prev, node, d = stack.pop()
        dist[node] = d

        d += 1

        for desc in tree[node]:
            if desc == prev:
                continue
            stack.append((node, desc, d))

    p = []

    return dist, p

A, path = dfs(1)
ind = A.index(max(A))
B, path = dfs(ind)

