n = int(input())
x = list(map(int, input().split()))

def is_prime(k, primes):

    if k < 2:
        return True
    
    sqrt = int(k**.5)
    for p in primes:
        if p > sqrt:
            return True
        if k % p == 0:
            return False
    
    return True

primes = [2, 3]
cursor = 5
while cursor <= 10**3:
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 2
    if is_prime(cursor, primes):
        primes.append(cursor)
    cursor += 3

dp = [0 for _ in range(16)]

for p in primes:
    if p > 15:
        break
    
    exp = 1
    while p**exp < 16:
        for k in range(p**exp, 16, p**exp):
            dp[k] += 1
        exp += 1
    print(dp)

res = [dp[v] for v in x]
print(*res)

"""
3
2 * 7
3 * 5
7
3 * 3
1 * 1
"""

# max_candidate = 1

# for v in x:
#     dp[v] += 1
#     dp[1] += 1

#     candidate = 1

#     for p in primes:

#         if v == 1:
#             break

#         while v % p == 0:
#             v //= p
#             dp[v] += 1
#             if dp[v] > 1 and v > max_candidate:
#                 max_candidate = v

#         if v <= max_candidate:
#             break

#         if is_prime(v, primes):
#             break

# print(max_candidate)