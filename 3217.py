from collections import deque
n = int(input())

grid = [[-1] * n for _ in range(n)]
grid[0][0] = 0

candidates = deque([(0, 0)])

while candidates:
    x, y = candidates.pop()

    moves = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
    for move in moves:
        cx, cy = x + move[0], y + move[1]
        if not (0 <= cx <= n - 1) or not (0 <= cy <= n - 1) or grid[cy][cx] != -1:
            continue
        grid[cy][cx] = grid[y][x] + 1
        candidates.appendleft((cx, cy))

for line in grid:
    print(*line)