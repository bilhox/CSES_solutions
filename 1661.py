from itertools import accumulate
from collections import defaultdict

X = 18349453871

n, x = map(int, input().split())
a = list(map(int, input().split()))
 
pref_sum = list(accumulate(a))
 
subed = defaultdict(int)
subed[X] = 1
counter = 0
 
for v in pref_sum:
    if (v - x) ^ X in subed:
        counter += subed[(v - x) ^ X]
    
    subed[v ^ X] += 1
 
print(counter)