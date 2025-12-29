MOD = 10**9 + 7

n = int(input())

res = 0
k = 1
while k <= n:
    j = n // (n // k)
    res = (res + (((j - k + 1) * (k + j)) // 2) * (n // k)) % MOD
    k = j + 1

print(res)