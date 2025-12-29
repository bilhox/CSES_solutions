from collections import defaultdict, OrderedDict
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

pref = [0 for _ in range(n)]
pref[0] = a[0] % n

for i in range(1, n):
    pref[i] = (pref[i - 1] + a[i]) % n

counter = 0
seen = OrderedDict()
seen[0] = 1

for v in pref:
    if (v - n) % n in seen:
        counter += seen[(v - n) % n]
    
    if v in seen:
        seen[v] += 1
    else:
        seen[v] = 1

print(counter)