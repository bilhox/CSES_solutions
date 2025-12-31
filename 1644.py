from itertools import accumulate
from math import inf

n, a, b = map(int, input().split())
x = list(map(int, input().split()))

pref = list(accumulate(x))

current_sum = -inf
best_sum = -inf

for v in x:
    current_sum = max(current_sum + v, v)
    best_sum = max(current_sum, best_sum)

print(pref)
print(best_sum)