import sys

n, q = map(int, input().split())
a = [0, 0] + list(map(int, input().split()))

N = 32
sparse = [[0] * (n + 1) for _ in range(N)]
sparse[0] = a

for i in range(1, N):
    for j in range(1, n + 1):
        ancestor = sparse[i - 1][j]
        sparse[i][j] = sparse[i - 1][ancestor]

result = []
for _ in range(q):
    a, k = map(int, input().split())

    v = a
    for i in range(32):
        if k & 1:
            v = sparse[i][v]
        k >>= 1 

    if v == 0:
        result.append(-1)
    else:
        result.append(v)

print(*result, sep="\n")