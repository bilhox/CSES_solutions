import sys
MOD = 1_000_000_007


# ======================================================================
# Method 1 (recommended): exact modular computation via resultants
# ======================================================================
# 2*cos(a*pi/(n+1)), a=1..n are exactly the eigenvalues of the path-graph
# adjacency matrix A_n. Its characteristic polynomial p_n(x) obeys the
# simple integer recurrence  p_0=1, p_1=x, p_k = x*p_{k-1} - p_{k-2}.
#
# The roots of p_n come in +/-lambda pairs (plus a single 0 if n is odd),
# so p_n is an even/odd function of x and can be written as
#   p_n(x) = x^(n mod 2) * H_n(x^2)
# where H_n is a monic integer polynomial of degree ceil(n/2) whose roots
# are exactly the ceil(n/2) distinct values  (2*cos(a*pi/(n+1)))^2.
#
# prod_{a,b} (lambda_a^2 + mu_b^2) over the half-ranges then equals (up to
# a sign) the resultant of H_n(y) and H_m(-y), computed here as the
# determinant of the Sylvester matrix, done entirely mod p.

def path_charpoly(n):
    """Coefficients (low->high degree) of the path-graph characteristic
    polynomial p_n(x), via p_k = x*p_{k-1} - p_{k-2}."""
    p_prev2 = [1]        # p_0
    if n == 0:
        return p_prev2
    p_prev1 = [0, 1]     # p_1
    for _ in range(2, n + 1):
        shifted = [0] + p_prev1          # x * p_{k-1}
        new = shifted[:]
        for i, c in enumerate(p_prev2):  # subtract p_{k-2}
            new[i] -= c
        p_prev2, p_prev1 = p_prev1, new
    return p_prev1


def half_poly(n):
    """Coefficients of H_n(y) (index = power of y), degree ceil(n/2), monic."""
    p = path_charpoly(n)
    if n % 2 == 0:
        return p[0::2]                # powers 0,2,4,... -> y^0,y^1,...
    else:
        return [0] + p[1::2]          # powers 1,3,5,... -> y^1,y^2,...


def poly_neg_y(coeffs):
    """Coefficients of f(-y) given coefficients of f(y)."""
    return [c if k % 2 == 0 else -c for k, c in enumerate(coeffs)]


def resultant_mod(f, g, mod):
    """Resultant of two integer polynomials, reduced mod p, via the
    determinant of the Sylvester matrix (Gaussian elimination mod p)."""
    def deg(c):
        d = len(c) - 1
        while d > 0 and c[d] % mod == 0:
            d -= 1
        return d

    df, dg = deg(f), deg(g)
    N = df + dg
    if N == 0:
        return 1 % mod

    M = [[0] * N for _ in range(N)]
    for i in range(dg):
        for j in range(df + 1):
            M[i][i + j] = f[df - j] % mod
    for i in range(df):
        for j in range(dg + 1):
            M[dg + i][i + j] = g[dg - j] % mod

    det = 1
    for col in range(N):
        piv = next((r for r in range(col, N) if M[r][col] % mod), None)
        if piv is None:
            return 0
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            det = (-det) % mod
        det = (det * M[col][col]) % mod
        inv = pow(M[col][col], mod - 2, mod)
        for row in range(col + 1, N):
            factor = (M[row][col] * inv) % mod
            if factor:
                for k in range(col, N):
                    M[row][k] = (M[row][k] - factor * M[col][k]) % mod
    return det % mod


def exact_method(n, m, mod=MOD):
    Hn = half_poly(n)
    Hm = half_poly(m)
    Gm = poly_neg_y(Hm)
    ceilN, ceilM = len(Hn) - 1, len(Hm) - 1
    res = resultant_mod(Hn, Gm, mod)
    sign = -1 if (ceilN * ceilM) % 2 else 1
    return (sign * res) % mod


# ======================================================================
if __name__ == "__main__":
    n, m = map(int, input().split())
    print(exact_method(n, m))