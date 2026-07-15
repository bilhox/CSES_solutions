n, a, b = map(int, input().split())

S = [0] * (b + 1)

for r in range(1, min(7, b + 1)):
    S[r] = 1

for k in range(n - 1):
    temp = [0] * (b + 1)

    for j in range(b + 1):
        if not S[j]:
            continue

        for r in range(1, 7):
            if j + r <= b:
                temp[j + r] += S[j]
    
    S = temp

print(f"{sum(S[a:b + 1]) / 6**n:.6f}")
