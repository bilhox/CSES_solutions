from math import inf
n = int(input())
x = list(map(int, input().split()))

best = -inf
current = 0
current_max = 0

for i in range(n):

    current ^= x[i]
    if x[i] > current_max:
        current_max = x[i]
    
    if current < x[i]:
        current = x[i]

    best = max(best, current)

print(best)