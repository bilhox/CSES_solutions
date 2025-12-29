import math

def count_l(r):
    v = 0
    for i in range(1, r + 1):
        v += i * math.comb(r, i)
    return v

n = int(input())
log = int(math.log2(n))
res = count_l(log)

h = bin(n)[3:][::-1]
set_count = h.count("1")
past_val = 0
sum_x = 0
for i, c in enumerate(h):
    if c == '1':
        sum_x += count_l(i + 1) - count_l(i) - past_val
    past_val = count_l(i + 1)
sum_x += 1

print(res + sum_x, res)