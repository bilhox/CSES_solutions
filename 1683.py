n, m = map(int, input().split())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    rev_graph[b].append(a)

visited = [0] * n

def dfs(s, graph):

    stack = [(s, False)]
    result = []

    while stack:
        node, processed = stack.pop()
        
        if processed:
            result.append(node)
            continue

        if visited[node]:
            continue
        
        visited[node] = 1

        if not processed:
            stack.append((node, True))
            for neigh in graph[node]:
                if not visited[neigh]:
                    stack.append((neigh, False))

    return result

res = []
for k in range(n):
    if not visited[k]:
        u = dfs(k, graph)
        # print(k, u)
        res.extend(u)
kingdoms = [0] * n
res.reverse()
count = 0
for v in res:
    if kingdoms[v]: continue

    count += 1
    stack = [v]
    kingdoms[v] = count
    while stack:
        node = stack.pop()

        for neigh in rev_graph[node]:
            if not kingdoms[neigh]:
                stack.append(neigh)
                kingdoms[neigh] = count
print(count)
print(*kingdoms)