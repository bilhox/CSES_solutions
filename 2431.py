q = int(input())
res = []
for _ in range(q):
    a = int(input())
    k = 0
    s = 9
    while(s < a):
        k += 1
        s += (k + 1) * 9 * 10**k
    
    s -= (k + 1) * 9 * 10**k
    u = 10**k + (a - s - 1) // (k + 1) if k != 0 else a
    res.append(str(u)[(a - s - 1) % (k + 1) if k != 0 else 0])

for el in res:
    print(el)