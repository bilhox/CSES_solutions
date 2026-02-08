n, m = map(int, input().split())

grid = [input() for _ in range(n)]

result = [["" for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        choices = {"A", "B", "C", "D"}
        choices.remove(grid[i][j])
        if i > 0:
            choices.discard(result[i - 1][j])
        if j > 0:
            choices.discard(result[i][j - 1])
        
        candidates = list(choices)
        result[i][j] = candidates[0]

for line in result:
    print("".join(line))
        