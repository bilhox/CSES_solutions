from collections import deque
n, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
 
states = [0] * (n + 1)
result = ["L"] * n
 
for l in range(1, n + 1):
    for v in p:
        if l - v < 0:
            break
        if not states[l - v]:
            states[l] = 1
            result[l - 1] = "W"
            break
 
print("".join(result))