import sys
a = [-1] * 10000001
b = [-1] * 10000001
for i in range(3200):
    for j in range(3200):
        if i**2 + j**2 > 10000000:
            break
        u = i**2 + j**2
        a[u] = i
        b[u] = j

t = int(input())
for line in sys.stdin:
    n = int(line)
    for k in range(n + 1):
        if a[n - k] != -1 and a[k] != -1:
            print(a[k], b[k], a[n - k], b[n - k])
            break

"""
pour tout e 
"""