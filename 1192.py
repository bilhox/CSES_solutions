n, m = map(int, input().split())

def dfs(lab, visited, pos):

    W = len(lab[0])
    H = len(lab)

    stack = [pos]
    visited[pos[1]][pos[0]] = True

    while stack != []:
        x, y = stack.pop()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            cx = max(0, min(x + dx, W - 1))
            cy = max(0, min(y + dy, H - 1))
            if not visited[cy][cx] and lab[cy][cx] == '.':
                stack.append((cx, cy))
                visited[cy][cx] = True

lab = [input() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
for j in range(n):
    for i in range(m):
        if lab[j][i] == "." and not visited[j][i]:
            count += 1
            dfs(lab, visited, (i, j))

print(count)