t = int(input())

def shift_array(a, shifting):
    temp = []
    for i in range(len(a)):
        temp.append(a[(i + shifting) % len(a)])
    return temp

for _ in range(t):
    n, a, b = map(int, input().split())
    if a + b > n or ((a == 0) ^ (b == 0)):
        print("NO")
        continue
    
    total_score = a + b
    rem = n - a - b

    if total_score == 1:
        print("NO")
        continue

    pref = [k for k in range(1, rem + 1)]
    print("YES")

    if rem == n:
        print(*pref)
        print(*pref)
        continue

    left = [k for k in range(rem + 1, n + 1)]
    print(*pref + left)
    right = shift_array(left, a)
    print(*pref + right)
"""
2 3 4 5
3 4 5 2
"""