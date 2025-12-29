n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
dp = [0] * (x + 1)

MOD = 10**9 + 7

for coin in p:
    if coin > x:
        break
    dp[coin] += 1

for k in range(min(p), x + 1):
    if dp[k] == 0:
        continue
    for coin in p:
        if k + coin > x:
            break
        dp[k + coin] = (dp[k + coin] + dp[k]) % MOD

print(dp[-1])