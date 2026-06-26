n = int(input())

MOD = 10**9 + 7

fact = [1]
for k in range(1, 2 * 10**6):
    fact.append((fact[-1] * k) % MOD)

def comb(n, k):
    return (fact[n] * pow(fact[n - k] * fact[k], -1, MOD)) % MOD

if n % 2 == 0:
    print((comb(n, n // 2) * pow(n // 2 + 1, -1, MOD)) % MOD)
else:
    print(0)