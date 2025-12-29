n = int(input())

MOD = 10**9 + 7

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

grid = [input() for _ in range(n)]
if grid[0][0] == "*" or grid[-1][-1] == "*":
    print(0)
    exit()

for i in range(n):
    for j in range(n):
        cell = grid[i][j]
        if cell == "*":
            continue
        s = 0
        if i > 0:
            s = dp[i - 1][j] % MOD
        if j > 0:
            s = (s + dp[i][j - 1]) % MOD
        
        dp[i][j] += s

print(dp[-1][-1])