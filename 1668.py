from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque([(1, 2)])
color = [0] * n
remaining = {k for k in range(2, n + 1)}

impossible = False

while remaining:

    if not queue:
        queue.appendleft((remaining.pop(), 2))

    node, c = queue.pop()
    remaining.discard(node)
    color[node - 1] = 1 + c % 2
    
    for neigh in adj[node]:
        if not color[neigh - 1]:
            queue.appendleft((neigh, 1 + c % 2))
        if color[neigh - 1] == color[node - 1]:
            impossible = True
    
    if impossible:
        break

if impossible:
    print("IMPOSSIBLE")
else:
    print(*color)