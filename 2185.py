from itertools import combinations

n, k = map(int, input().split())
primes = list(map(int, input().split()))


result = 0

for p in primes:
    result += n // p

minus = -1
for k in range(2, len(primes) + 1):
    for comb in combinations(primes, k):
        v = 1
        for p in comb:
            v *= p
        result += minus * (n // v)
    minus *= -1
    

print(result)