import numpy

n = int(input())

def prod_matrix(m1, m2):
    matrix = []
    for i in range(2):
        line = [0, 0]
        for j in range(2):
            line[j] = (m1[i][0] * m2[0][j] + m1[i][1] * m2[1][j]) % (10**9 + 7)
        matrix.append(line)
    return matrix

def expo_fast(matrix, n):
    if n == 1 or n == 0:
        return matrix
    else:
        if n % 2 == 1:
            m1 = expo_fast(matrix, (n - 1) // 2)
            return prod_matrix(matrix, prod_matrix(m1, m1))
        else:
            m1 = expo_fast(matrix, n // 2)
            return prod_matrix(m1, m1)

fib_m = [
    [1, 1],
    [1, 0]
]

if n != 0:
    m = expo_fast(fib_m, n)
    print(m[0][1])
else:
    print(0)