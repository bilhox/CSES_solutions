from sys import setrecursionlimit

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp1 = [0] * (n + 1) # No edge is connecting vertex to its children
dp2 = [0] * (n + 1) # An edge is connecting vertex to a child

def dfs():

    stack = [(-1, 1, False)]

    while stack:
        prev, s, computable = stack.pop()

        if tree[s] == [prev]:
            continue

        if not computable:
            stack.append((prev, s, True))
            for v in tree[s]:
                if v == prev: continue
                stack.append((s, v, False))
            continue

        r1 = 0

        for v in tree[s]:
            if v == prev: continue
            r1 += dp2[v]

        dp1[s] = r1

        for v in tree[s]:
            if v == prev: continue
            dp2[s] = max(dp2[s], 1 + dp1[v] + r1 - dp2[v])

"""
1
L 2
L 3
  L 4
  L 5
"""

dfs()
# print(dp1, dp2)
print(max(dp1[1], dp2[1]))