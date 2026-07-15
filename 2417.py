from math import comb
n = int(input())
x = list(map(int, input().split()))

def is_prime(primes, n):
    if n < 2:
        return False
    
    sqrt = int(n**.5)
    for p in primes:
        if p > sqrt:
            return True
        if n % p == 0:
            return False

    return True

primes = []
for k in range(2, 10**6):
    if is_prime(primes, k):
        primes.append(k)

SUP = max(x) + 1
mobius = [1] * SUP

for p in primes:
    for k in range(p**2, SUP, p**2):
        mobius[k] = 0

for p in primes:
    for k in range(p, SUP, p):
        mobius[k] *= -1

number_line = [0] * SUP
for v in x:
    number_line[v] += 1

divisors = [0] * SUP
for k in range(1, SUP):
    for i in range(k, SUP, k):
        divisors[k] += number_line[i]

total = 0
for k in range(1, SUP):
    total += mobius[k] * comb(divisors[k], 2)

print(total)