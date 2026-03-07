from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque([(1, 0)])
ancestors = {1:None}
visited = [False] * (n + 1)
distances = [float("inf")] * (n + 1)

while queue:
    node, dist = queue.pop()
    visited[node] = True
    if node == n:
        break

    for neigh in adj[node]:
        if not visited[neigh] and distances[neigh] > dist + 1:
            ancestors[neigh] = node
            distances[neigh] = dist + 1
            queue.appendleft((neigh, dist + 1))

if n not in ancestors:
    print("IMPOSSIBLE")
else:
    path = deque([n])
    while ancestors[path[0]] != None:
        path.appendleft(ancestors[path[0]])
    
    print(len(path))
    print(*path)