from collections import deque
n, m = map(int, input().split())
 
def bfs(graph, n):
 
    visited = [0] * n
    queue = deque([0])
    visited[0] = 1
 
    while queue:
        node = queue.pop()
        for neigh in graph[node]:
            if not visited[neigh]:
                queue.appendleft(neigh)
                visited[neigh] = 1
    return visited
 
graph = [set() for _ in range(n)]
in_degree = [0] * n
out_degree = [0] * n
used = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].add(b)
    out_degree[a] += 1
    in_degree[b] += 1
    used[a] = 1
    used[b] = 1
 
seen = bfs(graph, n)
 
if not all(seen[v] or not used[v] for v in range(n)):
    print("IMPOSSIBLE")
    exit()

if not all(in_degree[v] == out_degree[v] for v in range(1, n - 1)):
    print("IMPOSSIBLE")
    exit()

dg1 = out_degree[0] - in_degree[0]
dg2 = in_degree[n - 1] - out_degree[n - 1]

if dg1 == 0 or not (dg1 == dg2 == 1):
    print("IMPOSSIBLE")
    exit()
 
stack = [0]
path = []
while stack:
    node = stack[-1]
    if out_degree[node] == 0:
        path.append(node + 1)
        stack.pop()
    else:
        neigh = graph[node].pop()
        in_degree[neigh] -= 1
        out_degree[node] -= 1
        stack.append(neigh)
 
# print(kept)
path.reverse()
print(*path)