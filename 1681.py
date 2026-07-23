import sys

sys.setrecursionlimit(200005)

MOD = 10**9 + 7

n, m = map(int, input().split())
dp = [-1] * (n + 1)
graph = [[] for _ in range(n + 1)]
for line in sys.stdin:
    a, b = map(int, line.split())
    graph[b].append(a)

dp[1] = 1

def backtrack(v):

    total = 0
    for anc in graph[v]:
        if dp[anc] == -1:
            backtrack(anc)
        total = (dp[anc] + total) % MOD
    
    dp[v] = total

backtrack(n)
print(dp[n])