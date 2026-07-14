from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

in_degree = [0] * (n + 1)

for i in range(1, n + 1):
    for neigh in graph[i]:
        in_degree[neigh] += 1

# print(in_degree)

queue = deque([k for k in range(1, n + 1) if in_degree[k] == 0])
topo = []
while queue:
    node = queue.pop()
    topo.append(node)
    for neigh in graph[node]:
        in_degree[neigh] -= 1
        if in_degree[neigh] == 0:
            queue.appendleft(neigh)

if len(topo) != n:
    print("IMPOSSIBLE")
    exit()
print(*topo)