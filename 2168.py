from collections import deque

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
indices = [i for i in range(n)]

indices.sort(key=lambda i : ranges[i][0])

counter_contains = [0 for _ in range(n)]
counter_in = [0 for _ in range(n)]

max_end = None

for i in range(n):
    ind = indices[i]
    a, b = ranges[ind]

    if max_end == None:
        max_end = (a, b, ind)
        continue
    
    if b <= max_end[1]:
        if a == max_end[0] and b == max_end[1]:
            counter_in[max_end[2]] = 1
        counter_in[ind] = 1
    else:
        if a == max_end[0]:
            counter_in[max_end[2]] = 1
        max_end = (a, b, ind)

min_end = None

for i in range(n - 1, -1, -1):
    ind = indices[i]
    a, b = ranges[ind]

    if min_end == None:
        min_end = (a, b, ind)
        continue

    if b >= min_end[1]:
        if a == min_end[0] and b == min_end[1]:
            counter_contains[min_end[2]] = 1
        counter_contains[ind] = 1
    else:
        if a == min_end[0]:
            counter_contains[min_end[2]] = 1
        min_end = (a, b, ind)

print(*counter_contains)
print(*counter_in)