from collections import deque
from math import inf
import sys
n, m = map(int, input().split())
grid = [line for line in sys.stdin]

ancestors = [["#"] * m for _ in range(n)]
 
def bfs():
    
    visited = [[0] * m for _ in range(n)]
    queue = deque()

    start_pos = None
    for k in range(n):
        for l in range(m):
            if grid[k][l] == "M":
                visited[k][l] = 1
                queue.appendleft((k, l, 0))
            if grid[k][l] == "A":
                ancestors[k][l] = "A"
                visited[k][l] = 1
                start_pos = (k, l, 1)
    queue.appendleft(start_pos)

    while queue:
        y, x, t = queue.pop()
  
        for dy, dx, dd in [(1, 0, "D"), (-1, 0, "U"), (0, 1, "R"), (0, -1, "L")]:
            uy, ux = y + dy, x + dx
            if not 0 <= ux < m or not (0 <= uy < n):
                if t:
                    return (y, x)
                continue
            if grid[uy][ux] == "#":
                continue
            if not visited[uy][ux]:
                queue.appendleft((uy, ux, t))
                if t:
                    ancestors[uy][ux] = dd
                visited[uy][ux] = 1
    
    return -1, -1
 
def retrieve_path(i, j):
 
    p = []
    while ancestors[i][j] != "A":
        p.append(ancestors[i][j])
        d = ancestors[i][j]
        if d == "R":
            j -= 1
        elif d == "L":
            j += 1
        elif d == "U":
            i += 1
        else:
            i -= 1
    
    p.reverse()
    return "".join(p)
 
i, j = bfs()

# for line in ancestors:
#     print(line)
 
if i < 0:
    print("NO")
else:
    print("YES")
    u = retrieve_path(i, j)
    print(len(u))
    print(u)