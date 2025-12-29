from collections import defaultdict
from itertools import accumulate

n, x = map(int, input().split())
a = list(map(int, input().split()))

# left = 0
# right = 0

# counter = 0
# summation = 0

# while left < n:
#     if right != n:
#         summation += a[right]
#         right += 1
#     elif summation < x:
#         break
    
#     if summation == x:
#         counter += 1
#         summation -= a[left]
#         left += 1
#     elif summation > x:
#         while summation > x:
#             summation -= a[left]
#             left += 1
        
#         if summation == x:
#             counter += 1
#             summation -= a[left]
#             left += 1


# print(counter)

counter = 0
seen = defaultdict(int)
seen[0] = 0