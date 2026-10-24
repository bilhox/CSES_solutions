print(2**-10 - 2**-9, 2**-11 - 2**-10)

from itertools import accumulate
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    if n == 1:
        print("second")
        continue
