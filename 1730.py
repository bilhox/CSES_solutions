t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    xor_sum = 0
    for v in x:
        xor_sum ^= v
    if xor_sum:
        print("first")
    else:
        print("second")