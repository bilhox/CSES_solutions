n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
visited = [False] * (n + 1)

for k in range(1, n + 1):
    if visited[k]:
        continue

    progression = [k]
    visited[k] = True
    current = a[k]
    while not visited[current]:
        progression.append(current)
        visited[current] = True
        current = a[current]
    
    if dp[current] != 0:
        vc = dp[current] + 1
        while progression:
            u = progression.pop()
            dp[u] = vc
            vc += 1
    else:
        cycle_length = 0
        in_cycle = []
        while progression:
            u = progression.pop()
            in_cycle.append(u)
            cycle_length += 1
            if u == current:
                break
        
        for v in in_cycle:
            dp[v] = cycle_length
        
        vc = dp[current] + 1
        while progression:
            u = progression.pop()
            dp[u] = vc
            vc += 1

print(*dp[1:])