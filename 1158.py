n, x = map(int, input().split())
h = list(map(int, input().split()))
s = list(map(int, input().split()))

dp = [0] * (x + 1)

for vh, vs in zip(h, s):
    for j in range(x, vh - 1, -1):
        dp[j] = max(dp[j], dp[j - vh] + vs)

print(dp[x])