n = int(input())

def prod_mod(a, b, M):
    return ((a % M) * (b % M)) % M

MOD = 10**9 + 7
primes = [list(map(int, input().split())) for _ in range(n)]

count_div = 1
count_div_mod1 = 1
sum_div = 1
prod_div = 1

used = False
for p, k in primes:
    a = k + 1
    if not used and k % 2 == 1:
        a = (k + 1) // 2
        used = True
    count_div = prod_mod(count_div, k + 1, MOD)
    count_div_mod1 = prod_mod(count_div_mod1, a, MOD - 1)
    sum_div = prod_mod(sum_div, (pow(p, k + 1, MOD) - 1) * pow(p - 1, -1, MOD), MOD)

for p, k in primes:
    a = k
    if not used:
        a = k // 2
    term = pow(p, prod_mod(a, count_div_mod1, MOD - 1), MOD)
    prod_div = prod_mod(term, prod_div, MOD)

"""
a^b = n [MOD]
a^(b^(c [MOD - 1])) = n
"""

print(count_div, sum_div, prod_div)

