from collections import deque
n, q = map(int, input().split())
grid = [input() for _ in range(n)]

# print(grid[1])

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    queue = deque([(r1, c1)])
    dist = [[-1] * n for _ in range(n)]
    dist[r1][c1] = 0

    while queue:
        r, c = queue.pop()

        if r == r2 and c == c2:
            break

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            cr, cc = r + dr, c + dc
            # print(cr, cc)
            if dist[cr][cc] == -1 and grid[cr][cc] != ".":
                dist[cr][cc] = dist[r][c] + 1
                queue.appendleft((cr, cc))

    print(dist[r2][c2])