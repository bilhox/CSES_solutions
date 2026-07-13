from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(list)

for i, v in enumerate(a):
    d[v].append(i)

a.sort()

max_so_far = 0
for i in range(n - 1, -1, -1):
    ind = d[a[i]].pop()
    max_so_far = max(max_so_far, ind - i)

print(max_so_far)