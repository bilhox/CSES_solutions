import math
from collections import defaultdict, deque

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

dist = [0] * n

def bellman_ford(edges, n, s, ancestors):
    dist[s] = 0
    x = -1
    for _ in range(n):
        x = -1
        for a, b, c in edges:
            if dist[a] < math.inf and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
                ancestors[b] = a
                x = b
        # print(temp)
    
    return x

ancestors = defaultdict(int)
node = bellman_ford(edges, n, 0, ancestors)

if node == -1:
    print("NO")
else:
    print("YES")

    cycle = deque()

    visited = [0] * n
    ptr = node

    # print(ancestors)
    while True:
        cycle.appendleft(ptr + 1)
        if visited[ptr]:
            # print(cycle)
            while cycle[-1] != ptr + 1:
                cycle.pop()
            break
        visited[ptr] = 1
        ptr = ancestors[ptr]

    print(*cycle)