n = int(input())

"""
Number of derangement of size n = sum of (-1)^k * (number of permutation with k fixed points)
"""

MOD = 10**9 + 7
fact = [1]
for k in range(1, n + 1):
    fact.append((fact[-1] * k) % MOD)

total = 0

for k in range(n + 1):
    total = (total + (-1)**k * pow(fact[k], -1, MOD)) % MOD

print((fact[n] * total) % MOD)