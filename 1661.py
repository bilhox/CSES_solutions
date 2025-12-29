from itertools import accumulate
from collections import defaultdict
n, x = map(int, input().split())
a = list(map(int, input().split()))

pref_sum = list(accumulate(a))

subed = defaultdict(int)
subed[0] = 1
counter = 0

for v in pref_sum:
    if v - x in subed:
        counter += subed[v - x]
    
    subed[v] += 1

print(counter)
