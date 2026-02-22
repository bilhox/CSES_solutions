from heapq import *

n = int(input())
x = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = 0 # Minimum sequence end for an increasing sequence of length l
maxL = 1

for i in range(1, n):
    
    left = -1
    right = maxL
    middle = None

    while left + 1 < right:
        middle = (left + right) // 2
        if x[dp[middle]] < x[i]:
            left = middle
        else:
            right = middle
    
    maxL = max(maxL, left + 2)
    dp[left + 1] = i

print(maxL)