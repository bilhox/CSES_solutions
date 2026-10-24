n, m = map(int, input().split())

graph = [set() for _ in range(n)]
degree = [0] * n
first = None
for _ in range(m):
    a, b = map(int, input().split())
    if first is None:
        first = a
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)
    degree[a] += 1
    degree[b] += 1

deg = [len(v) % 2 for v in graph]
print(deg)
if sum(deg) not in [0, 2]:
    print("IMPOSSIBLE")
    exit()

kept = None

if sum(deg) == 2:
    u = deg.index(1)
    v = deg.index(1, u + 1)
    kept = (u, v)
    graph[u].add(v)
    graph[v].add(u)

stack = [first]
path = []
while stack:
    node = stack[-1]
    if degree[node] == 0:
        path.append(node + 1)
        stack.pop()
    else:
        neigh = graph[node].pop()
        degree[neigh] -= 1
        degree[node] -= 1
        graph[neigh].remove(node)
        stack.append(neigh)

print(*path)