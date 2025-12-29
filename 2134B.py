t = int(input())
res = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(lambda v : int(v), input().split()))
    mod = [v % (k + 1) for v in a]
    for i in range(n):
        a[i] += mod[i] * k
        mod[i] = a[i] % (k + 1)
    res.append(a)

for el in res:
    print(*el)