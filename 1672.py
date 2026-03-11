from collections import deque
from heapq import *
import sys


"""
Bad time, even tho it should be O((n + m)^2*log n), because
m = n², so it's O(m^3 log n)
"""

MAX = int(1e18)

# n, m, q = map(int, input().split())

# adj = [[] for _ in range(n + 1)]
# inp = iter(sys.stdin.readlines())
# for _ in range(m):
#     a, b, c = map(int, next(inp).split())
#     adj[a].append((b, c))
#     adj[b].append((a, c))

# def dijsktra(s):

#     dist = [MAX for _ in range(n)]
#     visited = [False for _ in range(n)]

#     dist[s] = 0

#     heap = [(dist[s], s)]
#     for k in range(n):
#         if k == s:
#             continue
#         heap.append((dist[k], k))

#     for i in range(n):
#         dis, v = heappop(heap)
#         while visited[v - 1]:
#             dis, v = heappop(heap)

#         if dist[v] == MAX:
#             break
        
#         for neigh in adj[1 + v]:
#             node, length = neigh
#             if dist[v] + length < dist[node - 1]:
#                 dist[node - 1] = dist[v] + length
#                 if not visited[node - 1]:
#                     heappush(heap, (dist[node - 1], node - 1))
    
#     return dist

# distances = []
# for k in range(n):
#     distances.append(dijsktra(k))

# for _ in range(q):
#     a, b = map(int, next(inp).split())
#     v = distances[a - 1][b - 1]
#     print(v if v != MAX else -1)

n, m, q = map(int, input().split())

inp = iter(sys.stdin.readlines())

grid = [[MAX]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, next(inp).split())
    if c < grid[a][b]:
        grid[a][b] = grid[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            v = grid[i][k] + grid[k][j]
            if v < grid[i][j]:
                grid[i][j] = grid[j][i] = v

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            grid[i][j] = 0
            continue
        if grid[i][j] == MAX:
            grid[i][j] = -1

for _ in range(q):
    a, b = map(int, next(inp).split())
    print(grid[a][b])
            
            