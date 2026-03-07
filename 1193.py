from collections import deque
import sys
n, m = map(int, input().split())
grid = sys.stdin.readlines()

start = None
end = None

for i in range(n):
    if "A" in grid[i]:
        start = i * m + grid[i].index("A")
    if "B" in grid[i]:
        end = i * m + grid[i].index("B")
    
    if start is not None and end is not None:
        break

ancestors = {start:None}
distances = [float("inf")] * (n * m)
queue = deque([(start, 0)])

while queue:
    node, dist = queue.pop()
    if grid[node // m][node % m] == "B":
        break

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        cx, cy = node % m + dx, node // m + dy
        if not (0 <= cx < m) or not (0 <= cy < n):
            continue
        neigh = cy * m + cx
        if grid[cy][cx] != "#"and distances[neigh] > dist + 1:
            ancestors[neigh] = node
            distances[neigh] = dist + 1
            queue.appendleft((neigh, dist + 1))

if end not in ancestors:
    print("NO")
else:
    print("YES")
    path = deque()
    node_from = end
    while node_from != start:
        dn = ancestors[node_from] - node_from
        if dn == -m:
            path.appendleft("D")
        elif dn == m:
            path.appendleft("U")
        elif dn == -1:
            path.appendleft("R")
        else:
            path.appendleft("L")
        node_from = ancestors[node_from]
    print(len(path))
    print("".join(path))