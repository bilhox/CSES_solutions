from bisect import *
s = []
tot = 0
for k in range(1, 10**6 + 5 * 10**5):
    tot += k
    s.append(tot)

def solve():
    n = int(input())
    ind = bisect_left(s, n)
    if s[ind] == n:
        return 1

    l = 0
    r = ind
    while l <= r:
        v = s[l] + s[r]
        if v > n:
            r -= 1
        elif v < n:
            l += 1
        else:
            return 2
    
    return 3

t = int(input())
for _ in range(t):
    print(solve())