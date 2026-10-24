from collections import defaultdict
from itertools import accumulate

X = 183883939741

n = int(input())
a = list(map(int, input().split()))

pref = [0 for _ in range(n)]
pref[0] = a[0] % n

for i in range(1, n):
    pref[i] = (pref[i - 1] + a[i]) % n

counter = 0
seen = defaultdict(int)
seen[X] = 1

for v in pref:
    if ((v - n) % n) ^ X in seen:
        counter += seen[((v - n) % n) ^ X]
    
    if v ^ X in seen:
        seen[v ^ X] += 1
    else:
        seen[v ^ X] = 1

print(counter)