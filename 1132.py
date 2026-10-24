import sys
from heapq import *

sys.setrecursionlimit(200001)

n = int(input())
tree = [[] for _ in range(n + 1)]

for line in sys.stdin:
    a, b = map(int, line.split())
    tree[a].append(b)
    tree[b].append(a)

dp = [(-1, 0)] * (n + 1)
dp2 = [(-1, 0)] * (n + 1)
dp3 = [0] * (n + 1)

def dfs(prev, s, h):
    for desc in tree[s]:
        if desc == prev: continue
        dfs(s, desc, h + 1)
        if dp[s] == (-1, 0):
            dp[s] = (desc, 1 + dp[desc][1])
        
        if dp[s][1] < 1 + dp[desc][1]:
            dp2[s] = dp[s]
            dp[s] = (desc, 1 + dp[desc][1])

dfs(-1, 1, 0)

result = [-1] * n
stack = [(0, 1)]

while stack:
    prev, node = stack.pop()

    for desc in tree[node]:
        if prev == desc: continue
        stack.append((node, desc))
        if dp[node][0] == desc:
            result[desc - 1] = max(dp[desc][1], 1 + dp2[node][1])