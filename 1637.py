n = int(input())

dp = [10**6 + 1 for _ in range(n + 1)]
dp[0] = 0

for i in range(n):
    
    actual_number = n - i
    digits = list(map(int, str(actual_number)))
    for digit in digits:
        dp[i + digit] = min(dp[i] + 1, dp[i + digit])

print(dp[-1])