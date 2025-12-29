n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
dp = [0] * (x + 1)
dp[0] = 1

MOD = 10**9 + 7

# for coin in p:
#     if coin > x:
#         break
#     dp[coin] += 1

# print(dp)

for coin in p:
    for w in range(coin, x + 1):
        dp[w] = (dp[w] + dp[w - coin]) % MOD

print(dp[-1])

"""
5 = 2 + 3, 5
6 = 2 + 2 + 2, 3 + 3
7 = 2 + 2 + 3, 5 + 2
8 = 2 + 2 + 2 + 2, 2 + 3 + 3, 5 + 3
9 = 5 + 2 + 2, 2 + 2 + 2 + 3, 3 + 3 + 3
"""