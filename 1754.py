t = int(input())
for _ in range(t):
    a, b = [int(v) for v in input().split()]
    r = abs(a - b)
    if a < b:
        a -= r
        b -= 2*r
    else:
        b -= r
        a -= 2*r
    
    if a == b == 0:
        print("YES")
        continue
    if a < 0:
        print("NO")
        continue

    a %= 3
    b %= 3
    if a == b == 0:
        print("YES")
    elif a == 2 and b == 1 or a == 1 and b == 2:
        print("YES")
    else:
        print("NO")