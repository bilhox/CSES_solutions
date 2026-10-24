n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
comp = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    comp[b].append(a)

bidirectional = [False] * (n + 1)
bidirectional[0] = True

for k in range(1, n + 1):
    if comp[k] and graph[k]:
        bidirectional[k] = True

def dfs(graph):
    visited = [False] * (n + 1)
    visited[0] = True
    stack = [1]
    visited[1] = True

    while stack:
        node = stack.pop()

        for neigh in graph[node]:
            if not visited[neigh]:
                visited[neigh] = True
                stack.append(neigh)
    
    return visited

temp1 = dfs(graph)
temp2 = dfs(comp)

if not all(bidirectional):
    print("NO")
    k = bidirectional.index(False)
    if graph[k]:
        print(graph[k][0], k)
    elif comp[k]:
        print(k, comp[k][0])
    else:
        print(k, [1, 2][k == 1])
elif not all(temp1):
    print("NO")
    a = temp1.index(False)
    b = temp1.index(True)
    print(f"{a} {b}")
elif not all(temp2):
    print("NO")
    a = temp2.index(False)
    b = temp2.index(True)
    print(f"{a} {b}")
else:
    print("YES")