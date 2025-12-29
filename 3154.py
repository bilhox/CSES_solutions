MOD = 10**9 + 7

n, m = map(int, input().split())
coefs = [list(map(int, input().split())) for _ in range(n)]

# Gauss pivot algorithm

from_line = 0

for i in range(m):

    if i >= n:
        break

    # We ensure that the line we use is correct for the pivot

    pivot_line = from_line
    while pivot_line < n and coefs[pivot_line][i] == 0:
        pivot_line += 1
    
    if pivot_line >= n:
        continue
    else:
        coefs[from_line], coefs[pivot_line] = coefs[pivot_line], coefs[from_line]

    # Iterate through lines
    for j in range(from_line + 1, n):
        # Iterate through line of coefs
        temp = coefs[j][i]
        for k in range(i, m + 1):
            to_sub = coefs[i][k] * temp
            coefs[j][k] = (coefs[i][i] * coefs[j][k] - to_sub) % MOD
    
    from_line += 1

# Here we try to find out if the system has a solution

found = None
for i in range(n - 1, -1, -1):
    if any(coefs[i][k] for k in range(m)):
        break
    elif coefs[i][-1]:
        print(-1)
        exit()

    if found == None:
        found = coefs[i][-1]
    elif found != coefs[i][-1]:
        print(-1)
        exit()

# In this case, we extract a valid solution ...

solution = [None for _ in range(m)]

for i in range(n - 1, -1, -1):

    right_side = coefs[i][-1]
    ind = []
    x_coef = None

    for j in range(m - 1, -1, -1):
        if coefs[i][j] == 0:
            continue

        if solution[j] == None:
            if x_coef:
                ind.append(j)
            else:
                x_coef = (j, coefs[i][j])
        else:
            right_side = (right_side - coefs[i][j] * solution[j]) % MOD
    
    if x_coef:
        index, coefficient = x_coef
        solution[index] = (right_side * pow(coefficient, -1, MOD)) % MOD
    
    for k in range(len(ind)):
        solution[ind[k]] = 0

# Set to 0 all coefficients that doesn't matter in the system    

for i in range(m):
    if solution[i] == None:
        solution[i] = 0

print(*solution)