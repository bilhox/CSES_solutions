import time
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
capacity = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] += c


def max_flow(source, sink):

    parent = [-1] * (n + 1)

    def augmenting_path(source, sink):
        nonlocal parent
        parent = [-1] * (n + 1)
        queue = deque([source])

        while queue:
            node = queue.pop()

            for child in graph[node]:
                w = capacity[node][child]
                if w <= 0 or parent[child] != -1: continue
                queue.appendleft(child)
                parent[child] = node
        
        return parent[sink] != -1
    
    flow = 0

    while augmenting_path(source, sink):
        
        dv = 10**25
        curr = sink
        while curr != source:
            dv = min(dv, capacity[parent[curr]][curr])
            curr = parent[curr]
        
        curr = sink
        while curr != source:
            capacity[parent[curr]][curr] -= dv
            capacity[curr][parent[curr]] += dv
            curr = parent[curr]

        flow += dv
    
    return flow

print(max_flow(1, n))
