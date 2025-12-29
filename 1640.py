n, x = map(int, input().split())
a = list(map(int, input().split()))

seen = {}
for i in range(n):
    if a[i] not in seen:
        seen[x - a[i]] = i
    else:
        print(i + 1, seen[a[i]] + 1)
        break
else:
    print("IMPOSSIBLE")

# import bisect

# def dicho_left(a, x):
#     left = -1
#     right = len(a)
#     middle = 0

#     while left + 1 < right:
#         middle = (left + right) // 2
#         if a[middle] <= x:
#             left = middle
#         else:
#             right = middle
    
#     return left

# def dicho(a, x, right_bound):
#     left = 0
#     right = right_bound
#     middle = 0

#     while left <= right:
#         middle = (left + right) // 2
#         if a[middle] < x:
#             left = middle + 1
#         elif a[middle] > x:
#             right = middle - 1
#         else:
#             return middle
    
#     return -1

# n, x = map(int, input().split())
# a = [int(v) for v in input().split()]
# b = sorted(a)
# d = {}
# seen = {}
# for i in range(n):
#     key = dicho_left(b, a[i])
#     if key not in seen:
#         d[key] = i
#         seen[key] = 1
#     else:
#         d[key - seen[key]] = i
#         seen[key] += 1

# r = n - 1
# l = 0

# impossible = False

# while r > 0:
#     v = dicho(b, x - b[r], r - 1)
#     if v != -1:
#         l = v
#         break
#     r -= 1
# else:
#     impossible = True

# if not impossible:
#     print(d[l] + 1, d[r] + 1)
# else:
#     print("IMPOSSIBLE")