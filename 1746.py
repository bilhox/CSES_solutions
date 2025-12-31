n, m = map(int, input().split())
x = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [[0] * (m + 1) for _ in range(n)]

dp[0] = [1] * (m + 1)

for i in range(n - 1):
    if x[i] != 0:
        to_spread = dp[i][x[i]]
        for k in range(max(1, x[i] - 1), min(m + 1, x[i] + 2)):
            dp[i + 1][k] = (dp[i + 1][k] + to_spread) % MOD
        continue

    for j in range(1, m + 1):
        to_spread = dp[i][j]
        for k in range(max(1, j - 1), min(m + 1, j + 2)):
            dp[i + 1][k] = (dp[i + 1][k] + to_spread) % MOD


print(sum(dp[-1][1:]) % MOD if x[-1] == 0 else dp[-1][x[-1]])