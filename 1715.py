from collections import Counter

MOD = 10**9 + 7

fact = [1]
for k in range(1, 10**6 + 1):
    fact.append((fact[-1] * k) % MOD)

def mul(N, G):
    den = 1
    for v in G:
        den = (den * fact[v]) % MOD
    
    return (fact[N] * pow(den, -1, MOD)) % MOD

s = input()
count = Counter(s)

g = []
for ch in count:
    g.append(count[ch])

print(mul(len(s), g))