import math
from heapq import *
from collections import defaultdict

def dijkstra_opt(graph, n, s):

    dist = defaultdict(lambda : math.inf)

    dist[s] = 0
    heap = [(0, s)]

    while heap:
        d_v, v = heappop(heap)

        if dist[v] != d_v:
            continue

        for neigh in graph[v]:
            node, length = neigh
            if dist[v] + length < dist[node]:
                dist[node] = dist[v] + length
                heappush(heap, (dist[node], node))
    
    return dist

"""
Dans l'état actuel, je ne peux pas faire juste un dijkstra.
Je vais faire un graphe d'états, en enrichissant les noeuds.
Un noeud a 2 états:
- 0 > le coupon n'a pas été utilisé jusque là
- 1 > le coupe a été utilisé jusque là

De A à B, je peux transitionner de :
- (A, 0) vers (B, 0) (coupon pas utilisé)
- (A, 0) vers (B, 1) (coupon utilisé sur A)
- (A, 1) vers (B, 1) (coupon déjà utilisé avant A)
"""

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[10 * a].append((10 * b, c))
    graph[10 * a].append((10 * b + 1, c // 2))
    graph[10 * a + 1].append((10 * b + 1, c))

distances = dijkstra_opt(graph, n, 10)
print(distances[n * 10 + 1])