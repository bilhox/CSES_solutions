import sys
data = sys.stdin.readlines()
n = int(data[0])
grid = data[1:]
visited = [[0] * n for _ in range(n)]
constructed = [grid[0][0]]
visited[0][0] = 1

for k in range(1, 2 * n - 1):

    best = "{"
    for i in range(min(k, n - 1), max(0, k - n + 1) - 1, -1):
        j = max(0, k - n + 1) + min(k, n - 1) - i
        if visited[i][j - 1] or visited[i - 1][j]:
            best = min(best, grid[i][j])

    constructed.append(best)

    for i in range(min(k, n - 1), max(0, k - n + 1) - 1, -1):
        j = max(0, k - n + 1) + min(k, n - 1) - i
        if best != grid[i][j]:
            continue
        if visited[i][j - 1] or visited[i - 1][j]:
            visited[i][j] = 1

print("".join(constructed))
