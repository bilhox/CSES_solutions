n = int(input())
vp_2 = 0
vp_5 = 0
k = 1
while n // 5**k != 0:
    vp_5 += n // 5**k
    k += 1
k = 1
while n // 2**k != 0:
    vp_2 += n // 2**k
    k += 1

print(min(vp_2, vp_5))