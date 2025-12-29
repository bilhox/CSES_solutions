n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
i = 0
j = n - 1
while i <= j:

    if (i == j and p[i] <= x) or p[i] + p[j] <= x:
        i += 1
    
    j -= 1
    ans += 1
print(ans)