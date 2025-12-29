n = int(input())
primes = []
primes_set = set()

def is_prime(k, pms):
    if k <= 1:
        return False
    
    for prime in pms:
        if prime > k**.5:
            break
        if k % prime == 0:
            return False
    
    return True

def paddic(k, p):
    r = 0
    while k % p**r == 0:
        r += 1
    return r - 1

for k in range(2, 10**3):
    if is_prime(k, primes):
        primes.append(k)

primes_set = set(primes)

def count_divisors(k):

    count = 0
    # r = int(k**.5)

    for p in range(1, int(k**.5) + 1):
        if k % p == 0:
            count += 1 + (p != k // p)

    # for p in primes:
    #     vp = paddic(k, p)
    #     k //= p ** vp
    #     count *= (vp + 1)

    #     if p > r:
    #         break

    #     if k in primes_set:
    #         count *= 2
    #         k = 1
    
    #     if k == 1:
    #         break
    
    # if k != 1:
    #     count *= 2

    return count

res = []

for _ in range(n):
    x = int(input())
    count = 0

    for p in range(1, int(x**.5) + 1):
        if x % p == 0:
            count += 1 + (p != x // p)
    res.append(str(count))

print("\n".join(res))