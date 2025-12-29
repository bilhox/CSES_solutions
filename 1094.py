n = int(input())
a = [int(v) for v in input().split()]
b = a.copy()
count_a = 0
count_b = 0
for i in range(1, n):
    if a[i] < a[i - 1]:
        count_a += a[i - 1] - a[i]
        a[i] = a[i - 1]

print(count_a)