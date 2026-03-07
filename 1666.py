from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque([1])
seen = [False] * (n + 1)
remaining = {k for k in range(2, n + 1)}
last_seen = None
roads = []

while remaining:

    if not queue:
        queue.appendleft(remaining.pop())
        roads.append((last_seen, queue[0]))

    node = queue.pop()
    last_seen = node
    seen[node] = True
    
    for neigh in adj[node]:
        if not seen[neigh]:
            queue.appendleft(neigh)
            remaining.discard(neigh)

print(len(roads))
for road in roads:
    print(*road)