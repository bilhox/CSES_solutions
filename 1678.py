from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topo_sort_check(graph, in_degree, n):
    queue = deque()
    done = [0] * n

    for v in range(n):
        if in_degree[v] == 0:
            done[v] = 1
            queue.appendleft(v)
    
    while queue:
    
        node = queue.pop()

        for neigh in graph[node]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                done[neigh] = True
                queue.appendleft(neigh)

    return {v for v in range(n) if not done[v]}

def bfs_cycle(graph, n, unchecked : set):

    s = None
    ancestors = [-1] * n
    queue = deque()

    while unchecked or queue:

        if not queue:
            s = unchecked.pop()
            queue.appendleft(s)

        node = queue.pop()

        for succ in graph[node]:
            if succ == s:
                ancestors[s] = node
                return ancestors, s

            if succ in unchecked:
                unchecked.discard(succ)
                ancestors[succ] = node
                queue.appendleft(succ)

    return ancestors, None

unchecked = topo_sort_check(graph, in_degree, n + 1)

if not unchecked:
    print("IMPOSSIBLE")
    exit()

# print(checked)
ancestors, start = bfs_cycle(graph, n + 1, unchecked)
# print(ancestors, start)

cycle = [start, ancestors[start]]
while cycle[-1] != start:
    cycle.append(ancestors[cycle[-1]])

cycle.reverse()

print(len(cycle))
print(*cycle)