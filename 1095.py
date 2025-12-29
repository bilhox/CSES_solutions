import sys
gen = iter(sys.stdin.read().strip().split())
n = int(next(gen))

def pow_mod(a, b, m):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res
res = [str(pow_mod(int(next(gen)), int(next(gen)), 10**9 + 7)) for _ in range(n)]
print("\n".join(res))