from heapq import *
from math import inf
from collections import deque, defaultdict
import sys
 
MOD = 10**9 + 7
 
def dijkstra(graph, n, s):
 
    dist = [inf] * n
    paths = [0] * n
    min_p = [inf] * n
    max_p = [-inf] * n
 
    dist[s] = 0
    paths[s] = 1
    min_p[s] = 0
    max_p[s] = 0
    heap = [(0, s)]
    
    while heap:
        d, node = heappop(heap)
 
        if dist[node] != d:
            continue
 
        for neigh, weight in graph[node]:
            if dist[node] + weight < dist[neigh]:
                dist[neigh] = dist[node] + weight
                paths[neigh] = paths[node]
                heappush(heap, (dist[neigh], neigh))
                min_p[neigh] = min_p[node] + 1
                max_p[neigh] = max_p[node] + 1
            elif dist[node] + weight == dist[neigh]:
                paths[neigh] = (paths[node] + paths[neigh]) % MOD
                min_p[neigh] = min(min_p[neigh], min_p[node] + 1)
                max_p[neigh] = max(max_p[neigh], max_p[node] + 1)
    
    return dist, paths, min_p, max_p
 
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for line in sys.stdin:
    a, b, c = map(int, line.split())
    graph[a].append((b, c))
 
distances, p, mp, Mp = dijkstra(graph, n + 1, 1)
 
print(distances[-1], p[-1], mp[-1], Mp[-1])