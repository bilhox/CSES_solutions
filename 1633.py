n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
dp[0] = 1
for i in range(2, n + 1):
    dp[i] = 0
    for k in range(1, 7):
        if i - k >= 0:
            dp[i] += dp[i - k]
    dp[i] %= 10**9 + 7

print(dp[-1])