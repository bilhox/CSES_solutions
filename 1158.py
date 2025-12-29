n, x = map(int, input().split())
h = list(map(int, input().split()))
s = list(map(int, input().split()))

dp = [0 for _ in range(x + 1)]
cost = [0 for _ in range(x + 1)]

for i in range(n):
    if h[i] <= x:
        dp[h[i]] = s[i]

for i in range(1, n):
    for j in range(x + 1):
        if j + h[i] <= x and dp[j] != 0:
            dp[j + h[i]] = max(dp[j + h[i]], dp[j + h[i]] + s[i])

print(max(dp))