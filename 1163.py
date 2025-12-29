from heapq import *
from collections import defaultdict

x, n = map(int, input().split())
traffic_lights = map(int, input().split())

def dicho(a, u):

    left = -1
    right = len(a)
    middle = None

    while left + 1 < right:
        middle = (left + right) // 2
        if a[middle] < u:
            left = middle
        else:
            right = middle
    
    return right

a = [0, x]
count = defaultdict(int)
heap = []
results = []

for lights in traffic_lights:
    index = dicho(a, lights)
    a.insert(index, lights)
    count[a[index + 1] - a[index - 1]] -= 1
    count[a[index + 1] - a[index]] += 1
    count[a[index] - a[index - 1]] += 1

    heappush(heap, a[index] - a[index + 1])
    heappush(heap, a[index - 1] - a[index])

    result = -heappop(heap)

    while count[result] == 0:
        result = -heappop(heap)
    
    heappush(heap, -result)
    results.append(result)
print(count)
print(*results)