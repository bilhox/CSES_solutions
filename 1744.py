a, b = map(int, input().split())

dp = [[0] * (a) for _ in range(b)]

for i in range(b):
    dp[i][0] = i

for j in range(a):
    dp[0][j] = j

for i in range(1, b):

    for j in range(1, a):

        if j == i:
            dp[i][j] = 0
            continue
        
        min_left = float("inf")
        min_top = float("inf")

        for k in range(j // 2 + 1):
            min_left = min(min_left, dp[i][k] + dp[i][j - k - 1])
        
        for k in range(i // 2 + 1):
            min_top = min(min_top, dp[k][j] + dp[i - k - 1][j])
        
        dp[i][j] = min(min_left, min_top) + 1

# for l in dp:
#     print(l)

print(dp[-1][-1])