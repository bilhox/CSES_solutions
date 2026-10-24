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
degree = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)
    degree[a] += 1
    degree[b] += 1

deg = [len(v) % 2 for v in graph]

seen = bfs(graph, n)

if sum(deg) != 0 or not all(seen[v] or degree[v] == 0 for v in range(n)):
    print("IMPOSSIBLE")
    exit()

stack = [0]
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

# print(kept)

print(*path)