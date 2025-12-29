import sys
n = int(input())

MOD = 10**9 + 7
factorials = [1] * (10**6 + 1)

for k in range(1, 10**6 + 1):
    factorials[k] = (factorials[k - 1] * k) % MOD

output = [0] * n
data = (map(int, line.strip().split()) for line in sys.stdin.readlines())

k = 0
for line in data:
    a, b = line
    output[k] = str((factorials[a] * pow(factorials[a - b] * factorials[b], -1, MOD)) % MOD)
    k += 1

print("\n".join(output))

"""
comb(n, p) = comb(n - 1, p) + comb(n - 1, p - 1)
n = fact(n) * inv(fact(n - k) * fact(k)) [MOD]
"""