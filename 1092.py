n = int(input())
if (n * (n + 1)) // 2 % 2 == 1:
    print("NO")
else:
    print("YES")
    a = []
    b = []
    sum_a = 0
    for k in range(n, 0, -1):
        if sum_a + k <= (n * (n + 1)) // 4:
            a.append(k)
            sum_a += k
        else:
            b.append(k)
    
    print(len(a))
    print(*reversed(a))
    print(len(b))
    print(*reversed(b))