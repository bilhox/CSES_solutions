from itertools import accumulate
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) == 0:
        print(0)
        continue

    print(2 * max(a) - sum(a) if 2 * max(a) > sum(a) else 1)
        