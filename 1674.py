n = int(input())
tree = [[] for _ in range(n + 1)]
l = list(map(int, input().split()))
for i in range(n - 1):
    v = l[i]
    tree[v].append(i + 2)

dp = [0] * n
stack = [(1, False)]

while stack:
    s, state = stack.pop()
    if not state:
        if not tree[s]:
            continue
        stack.append((s, True))
        for neigh in tree[s]:
            stack.append((neigh, False))
    
    else:
        for neigh in tree[s]:
            dp[s - 1] += dp[neigh - 1]
        dp[s - 1] += len(tree[s])

print(*dp)
