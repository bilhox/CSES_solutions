import bisect

n, k = [int(v) for v in input().split()]
x, a, b, c = [int(v) for v in input().split()]
dp_l = [(x, x)]
xor_s = 0
r = 0
for i in range(1, n + 1):
    x = (a * x + b) % c
    if len(dp_l) < k:
        dp_l.append((x, min(x, dp_l[-1][1])))
    else:
        last_el = dp_l[r - 1]
        xor_s ^= last_el[1]
        dp_l[r] = (x, min(x, last_el[1]))
        r = (r + 1) % k
    print(dp_l)
 
print(xor_s)
