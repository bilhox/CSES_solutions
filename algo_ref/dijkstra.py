import math
from collections import defaultdict

def dijkstra(graph, n, s, path):

    dist = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]

    path[s] = -1
    dist[s] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if not visited[j] and (v == -1 or dist[j] < dist[v]):
                v = j
        
        if dist[v] == math.inf:
            break
        
        visited[v] = True
        for neigh in graph[v]:
            node, length = neigh
            if dist[v] + length < dist[node]:
                dist[node] = dist[v] + length
                path[node] = v

n = int(input())
q = int(input())

graph = defaultdict(list)
for _ in range(q):
    a, b, c = [int(v) for v in input().split()]
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

path = [-1 for _ in range(n)]
print(graph)
dijkstra(graph, n, 0, path)
print(path)