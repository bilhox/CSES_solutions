n, x = map(int, input().split())
c = sorted(map(int, input().split()))
dp = [x + 1] * x
dp[0] = 0
for i in range(min(c), x + 1):
    for j in range(n):
        if i - c[j] < 0:
            break
        dp[i] = min(1 + dp[i - c[j]], dp[i])

if dp[-1] != x + 1:
    print(dp[-1])
else:
    print(-1)