from bisect import *
n = int(input())

projects = [list(map(int, input().split())) for _ in range(n)]
indices = [k for k in range(n)]

indices.sort(key=lambda j : projects[j][1])

endpoints = [projects[i][1] for i in indices]
dp = {}

max_so_far = None

for i in indices:
    a, b, c = projects[i]
    before = bisect_left(endpoints, a) - 1
    last = endpoints[before]

    if before < 0:
        dp[b] = max(dp[b], c) if b in dp else c
        if max_so_far is None or max_so_far[1] < dp[b]:
            max_so_far = (b, dp[b])
        dp[b] = max(dp[b], max_so_far[1])
        continue

    last_value = dp[last]

    if max_so_far is not None and max_so_far[0] < last:
        last_value = max(max_so_far[1], dp[last])
    
    if b not in dp:
        dp[b] = last_value + c
    else:
        dp[b] = max(dp[b], last_value + c)
    
    if max_so_far is None or max_so_far[1] < dp[b]:
        max_so_far = (b, dp[b])
    else:
        dp[b] = max(max_so_far[1], dp[b])


print(max(dp[k] for k in dp))