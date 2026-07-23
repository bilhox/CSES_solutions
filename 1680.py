from heapq import *
from math import inf
from collections import deque
import sys

def topo_sort_dp(graph, n, s):
    
    dp = [-inf] * n
    ancestors = {}
    dp[s] = 0
    ancestors[s] = -1

    in_degree = [0] * n
    for v in range(n):
        for d in graph[v]:
            in_degree[d] += 1

    queue = deque([v for v in range(n) if in_degree[v] == 0])
    topo = []

    while queue:
        node = queue.pop()
        topo.append(node)

        for neigh in graph[node]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                queue.appendleft(neigh)
    
    for v in topo:
        for neigh in graph[v]:
            if dp[v] + 1 > dp[neigh]:
                dp[neigh] = dp[v] + 1
                ancestors[neigh] = v
        
    return dp[-1], ancestors


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for line in sys.stdin:
    a, b = map(int, line.split())
    graph[a].append(b)

distance, ancestors = topo_sort_dp(graph, n + 1, 1)
if distance == -inf:
    print("IMPOSSIBLE")
else:
    print(distance + 1)
    p = []
    curr = n
    while curr in ancestors:
        p.append(curr)
        curr = ancestors[curr]
    p.reverse()
    print(*p)