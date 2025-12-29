import math
n = int(input())
a = [int(v) for v in input().split()]
a.sort()

med = a[n // 2]

best = 0
for i in range(n):
    best += abs(a[i] - med)

print(best)