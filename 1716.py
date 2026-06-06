from collections import Counter

MOD = 10**9 + 7

fact = [1]
for k in range(1, 2 * 10**6 + 1):
    fact.append((fact[-1] * k) % MOD)

def comb(N, K):
    return (fact[N] * pow(fact[N - K] * fact[K], -1, MOD)) % MOD

n, m = map(int, input().split())

print(comb(n + m - 1, m))