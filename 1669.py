from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [(1, None)]
seen = [False] * (n + 1)
remaining = {k for k in range(1, n + 1)}
ancestors = {1:None}

endpoints = []

while remaining:

    if not stack:
        next_node = remaining.pop()
        stack.append((next_node, None))
        ancestors[next_node] = None

    node, node_from = stack.pop()
    seen[node] = True
    remaining.discard(node)
    found_cycle = False
    
    for neigh in adj[node]:
        if node_from == neigh:
            continue
        if not seen[neigh]:
            stack.append((neigh, node))
            ancestors[neigh] = node
        else:
            endpoints = [node, neigh]
            found_cycle = True
    
    if found_cycle:
        break
    
if not endpoints:
    print("IMPOSSIBLE")
    exit()

path1 = deque([endpoints[0]])
while ancestors[path1[0]]:
    path1.appendleft(ancestors[path1[0]])

set_path1 = set(path1)
path2 = [endpoints[1]]
first_common = None
while path2[-1]:
    if path2[-1] in set_path1:
        first_common = path2[-1]
        break
    path2.append(ancestors[path2[-1]])

pushable = False
for node in path1:
    if pushable:
        path2.append(node)
    if node == first_common:
        pushable = True

path2.append(path2[0])

print(len(path2))
print(*path2)