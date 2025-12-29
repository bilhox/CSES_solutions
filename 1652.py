n, q = map(int, input().split())

pref_sum = [[0] * n for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(n):
        if j > 0:
            pref_sum[i][j] += pref_sum[i][j - 1]
        if line[j] == "*":
            pref_sum[i][j] += 1

for i in range(n):
    for j in range(n):
        if i > 0:
            pref_sum[i][j] += pref_sum[i - 1][j]

result = []

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    extra = 0

    if x1 != 1:
        extra += pref_sum[y2 - 1][x1 - 2]
    if y1 != 1:
        extra += pref_sum[y1 - 2][x2 - 1]
        if x1 != 1:
            extra -= pref_sum[y1 - 2][x1 - 2]

    result.append(pref_sum[y2 - 1][x2 - 1] - extra)

for r in result:
    print(r)