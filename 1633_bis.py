def prod_matrix(m1, m2):
    matrix = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            matrix[i][j] = sum(m1[i][k] * m2[k][j] for k in range(6)) % (10**9 + 7)
    return matrix

def expo_fast(matrix, n):
    if n <= 1:
        return matrix
    else:
        if n % 2 == 1:
            m1 = expo_fast(matrix, (n - 1) // 2)
            return prod_matrix(matrix, prod_matrix(m1, m1))
        else:
            m1 = expo_fast(matrix, n // 2)
            return prod_matrix(m1, m1)

def print_matrix(matrix, name):
    print(f"Matrix {name} :")
    for l in matrix:
        print(*l)

n = int(input())

a = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

x = [
    [32],
    [16],
    [8],
    [4],
    [2],
    [1]
]

if n <= 6:
    print(x[6 - n][0])
else:
    m = expo_fast(a, n - 6)
    c = prod_matrix(m, x)
    print(c[0][0])