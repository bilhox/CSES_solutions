n = int(input())
a = list(map(int, input().split()))
a_bis = [0 for _ in range(n)]
bij = {}
a_bis[0] = a[0]
bij[a[0]] = a_bis[0]
for i in range(1, n):
    a_bis[i] = a[i] + a_bis[i - 1]
    bij[a[i]] = a_bis[i]

r = 1
for i in range(2, n + 1):
    if bij[i] < bij[i - 1]:
        r += 1
print(r)