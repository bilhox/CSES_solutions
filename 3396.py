def is_prime(k, primes):

    v = int(k**.5)
    for p in primes:
        if p > v:
            break
        if k % p == 0:
            return False
    
    return True

primes = [2, 3]
cursor = 5
upper_bound = 8 * 10**5
while cursor <= upper_bound:
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 2
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 4

t = int(input())
res = []
for _ in range(t):
    n = int(input()) + 1
    while not is_prime(n, primes):
        n += 1
    res.append(str(n))

print("\n".join(res))
    