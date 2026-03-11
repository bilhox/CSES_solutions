from collections import deque
from heapq import *

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

# heapify(edges)

# dsu = DSU([k for k in range(1, n + 1)])

# count = 0

# while edges:
#     c, a, b = heappop(edges)
#     if not dsu.is_same_set(a, b):
#         count += 1
#         adj[a].append((b, c))
#         dsu.union(a, b)


dist = [float("inf") for _ in range(n)]
visited = [False for _ in range(n)]

dist[0] = 0

heap = [(dist[k], k) for k in range(n)]
heapify(heap)

for i in range(n):
    v = heappop(heap)[1]
    while visited[v]:
        v = heappop(heap)[1]
    
    if dist[v] == float("inf"):
        break
    
    visited[v] = True
    for neigh in adj[1 + v]:
        node, length = neigh
        if dist[v] + length < dist[node - 1]:
            dist[node - 1] = dist[v] + length
            if not visited[node - 1]:
                heappush(heap, (dist[node - 1], node - 1))

print(*dist)