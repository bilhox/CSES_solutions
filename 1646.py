from itertools import accumulate
n, q = map(int, input().split())
a = list(map(int, input().split()))
pref = [0] + list(accumulate(a))
for _ in range(q):
    l, r = map(int, input().split())
    print(pref[r] - pref[l - 1])