n, m, k = map(int, input().split())
a = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]
attributed = {}
b.sort()
a.sort()
i = 0
j = 0
ans = 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= k:
        i += 1
        j += 1
        ans += 1
    else:
        if b[j] - a[i] > k:
            i += 1
        else:
            j += 1

print(ans)

