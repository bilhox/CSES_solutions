n = int(input())
res = []
for k in range(1, n + 1):
    count = 0
    if k >= 5:
        #full square
        count += ((k**2 - 5**2) + 16) * (k - 4)**2
        #one external line missing
        count += 4 * (13 + (k**2 - 20)) * (k - 4) + 4 * (10 + (k**2 - 15)) * (k - 4)
        count += 4 * (11 + (k**2 - 16))
        count += 8 * (8 + (k**2 - 13))
        #corners
        count += 4 * (6 + (k**2 - 9))
        # pure luck
        count //= 2
        count += 4
    elif k == 2:
        count = 6
    elif k == 3:
        count = 28
    elif k == 4:
        count = 96
    res.append(count)

for el in res:
    print(el)
    
