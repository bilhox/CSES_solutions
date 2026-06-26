from math import prod
from collections import defaultdict

MOD = 10**9 + 7

def is_prime(n, primes):
    if n < 2:
        return False
    
    sqrt = int(n**.5)
    for p in primes:
        if p > sqrt:
            return True
        if n % p == 0:
            return False
    
    return True

primes = [2, 3]
cursor = 5
while cursor <= 2 * 10**5:
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 2
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 4


n = int(input())
p = [0] + list(map(int, input().split()))

visited = [False] * (n + 1)
cycle_lengths = []

for k in range(1, n + 1):
    if not visited[k]:
        visited[k] = True
        curr = k
        r = 1
        while not visited[p[curr]]:
            r += 1
            curr = p[curr]
            visited[curr] = True
        cycle_lengths.append(r)

cycle_lengths = list(set(cycle_lengths))
factors = {}

# print(cycle_lengths)

for v in cycle_lengths:
    for p in primes:
        
        exp = 0
        while v % p == 0:
            exp += 1
            v //= p
        
        if exp > 0:
            if p in factors:
                if factors[p] < exp:
                    factors[p] = exp
            else:
                factors[p] = exp

        if is_prime(v, primes):
            if v not in factors:
                factors[v] = 1
            break

        if v == 1:
            break

steps = 1
# print(factors)
for p in factors:
    steps = (steps * pow(p, factors[p], MOD)) % MOD
print(steps)