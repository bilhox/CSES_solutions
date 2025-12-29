n, k = [int(v) for v in input().split()]
x, a, b, c = [int(v) for v in input().split()]
sum_l = [x]
sum_x = x
xor_s = 0
r = 0
for i in range(1, n + 1):
    x = (a * x + b) % c
    if len(sum_l) < k:
        sum_l.append(x)
    else:
        xor_s ^= sum_x
        sum_x -= sum_l[r]
        sum_l[r] = x
        r = (r + 1) % k
    sum_x += x
 
print(xor_s)
