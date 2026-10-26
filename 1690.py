import sys
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
MOD = 10**9 + 7

graph = [[] for _ in range(n)]
for i in range(1, m + 1):
    a, b = int(data[2 * i]), int(data[2 * i + 1])
    graph[a - 1].append(b - 1)

dp = [[0] * (1 << n) for _ in range(n)]
dp[0][1] = 1

for state in range(1, (1 << n), 2):
    for node in range(n - 1):
        if dp[node][state] == 0:
            continue
        for neigh in graph[node]:
            new_state = state ^ (1 << neigh)
            dp[neigh][new_state] += dp[node][state]
            # dp[neigh][new_state] %= MOD

print(dp[n - 1][(1 << n) - 1] % MOD)
