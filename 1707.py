import math
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, s, n):

    queue = deque([(-1, s, 0)])

    for _ in range(n):
        prev, node, curr = queue.pop()

        if node == s and curr > 2:
            return curr

        for neigh in graph[node]:
            if neigh == prev: continue
            queue.appendleft((node, neigh, curr + 1))
    
    print(queue)
    return math.inf

print(bfs(graph, 1, n + 1))
