from collections import Counter

n = int(input())
x = list(map(int, input().split()))

sx = Counter(x)

sup = max(x)
max_so_far = 1
for k in range(1, sup + 1):
    total = 0
    for d in range(k, sup + 1, k):
        if d in sx:
            total += sx[d]
    if total > 1:
        max_so_far = k

print(max_so_far)