import math
from collections import deque

n, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n)] # Graphe orienté non pondéré, pour savoir si d'un cycle on peut aller à n
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))
    graph[a - 1].append(b - 1)

dist = [-math.inf for _ in range(n)]
dist[0] = 0
for _ in range(n - 1):
    for edge in edges:
        if dist[edge[0]] > -math.inf:
            dist[edge[1]] = max(dist[edge[1]], dist[edge[0]] + edge[2])

colored = []
for edge in edges:
    if dist[edge[0]] > -math.inf and dist[edge[1]] < dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        colored.append(edge[1])

linked = True
visited = [False] * n
def dfs(s):
    queue = deque([s])
    while queue:
        node = queue.pop()
        visited[node] = True
        if node == n - 1:
            return False
        for neigh in graph[node]:
            if not visited[neigh]:
                queue.append(neigh)
    return True

for node in colored:
    if not visited[node] and not dfs(node):
        linked = False
        break

if not linked:
    print(-1)
else:
    print(dist[-1])