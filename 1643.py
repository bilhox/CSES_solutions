n = int(input())
a = list(map(int, input().split()))

sumx = -float("inf")
best = -float("inf")

for v in a:
    sumx = max(sumx + v, v)
    best = max(sumx, best)

print(best)
