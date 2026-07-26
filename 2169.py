from bisect import *
from random import getrandbits
import sys

X = 31443539979727

n = int(input())
data = []
mapped = []
for line in sys.stdin:
    a, b = map(int, line.split())
    data.append((a, b))
    mapped.append(b)

mapped = sorted(mapped)
compression = {v ^ X : i for i, v in enumerate(mapped)}

segments = []

for i in range(n):
    l, r = data[i]
    segments.append((l, compression[r ^ X], i))

segments.sort(key=lambda u : (u[0], -u[1]))

def query(bit, index):
    ans = 0
    while index > 0:
        ans += bit[index]
        index -= index & -index
    return ans

def update(bit, index, delta):
    while index < len(bit):
        bit[index] += delta
        index += index & -index

contains = [0] * n
is_in = [0] * n
bit = [0] * (n + 1)
for i in range(n):
    a, b, ind = segments[i]
    is_in[ind] = i - query(bit, b)
    update(bit, b + 1, 1)

bit = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    a, b, ind = segments[i]
    contains[ind] = query(bit, b + 1)
    update(bit, b + 1, 1)
    
print(*contains)
print(*is_in)