import random
from math import gcd
from itertools import product
import time


class GaussianInt:
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = int(re)
        self.im = int(im)

    def __add__(self, o):
        return GaussianInt(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return GaussianInt(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return GaussianInt(self.re * o.re - self.im * o.im,
                            self.re * o.im + self.im * o.re)

    def conj(self):
        return GaussianInt(self.re, -self.im)

    def norm(self):
        return self.re * self.re + self.im * self.im


def _round_div(n, d):
    q, r = divmod(n, d)
    if 2 * r >= d:
        q += 1
    return q


def gaussian_gcd(a: GaussianInt, b: GaussianInt) -> GaussianInt:
    while b.norm() != 0:
        denom = b.norm()
        prod = a * b.conj()
        q = GaussianInt(_round_div(prod.re, denom), _round_div(prod.im, denom))
        r = a - q * b
        a, b = b, r
    return a


class HurwitzQuaternion:
    __slots__ = ("tw", "tx", "ty", "tz")

    def __init__(self, tw, tx, ty, tz):
        self.tw, self.tx, self.ty, self.tz = tw, tx, ty, tz

    @classmethod
    def from_ints(cls, w, x, y, z):
        return cls(2 * w, 2 * x, 2 * y, 2 * z)

    def __add__(self, o):
        return HurwitzQuaternion(self.tw + o.tw, self.tx + o.tx,
                                  self.ty + o.ty, self.tz + o.tz)

    def __sub__(self, o):
        return HurwitzQuaternion(self.tw - o.tw, self.tx - o.tx,
                                  self.ty - o.ty, self.tz - o.tz)

    def __mul__(self, o):
        w1, x1, y1, z1 = self.tw, self.tx, self.ty, self.tz
        w2, x2, y2, z2 = o.tw, o.tx, o.ty, o.tz
        rw = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        rx = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        ry = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
        rz = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
        return HurwitzQuaternion(rw // 2, rx // 2, ry // 2, rz // 2)

    def conjugate(self):
        return HurwitzQuaternion(self.tw, -self.tx, -self.ty, -self.tz)

    def norm(self):
        s = self.tw ** 2 + self.tx ** 2 + self.ty ** 2 + self.tz ** 2
        return s // 4

    def is_lipschitz(self):
        return self.tw % 2 == 0 and self.tx % 2 == 0 and self.ty % 2 == 0 and self.tz % 2 == 0

    def as_ints(self):
        return (self.tw // 2, self.tx // 2, self.ty // 2, self.tz // 2)


def quaternion_gcrd(alpha: HurwitzQuaternion, beta: HurwitzQuaternion) -> HurwitzQuaternion:
    while beta.norm() != 0:
        D = beta.norm()
        prod = alpha * beta.conjugate()
        d = 2 * D

        cw, cx, cy, cz = (_round_div(t, d) for t in (prod.tw, prod.tx, prod.ty, prod.tz))
        hw, hx, hy, hz = (_round_div(2 * t - d, 2 * d) for t in (prod.tw, prod.tx, prod.ty, prod.tz))

        dist_int = sum((t - c * d) ** 2 for t, c in
                        zip((prod.tw, prod.tx, prod.ty, prod.tz), (cw, cx, cy, cz)))
        dist_half = sum((t - D - h * d) ** 2 for t, h in
                         zip((prod.tw, prod.tx, prod.ty, prod.tz), (hw, hx, hy, hz)))

        if dist_int <= dist_half:
            q = HurwitzQuaternion(2 * cw, 2 * cx, 2 * cy, 2 * cz)
        else:
            q = HurwitzQuaternion(2 * hw + 1, 2 * hx + 1, 2 * hy + 1, 2 * hz + 1)

        remainder = alpha - q * beta
        alpha, beta = beta, remainder
    return alpha


_HURWITZ_UNITS = None


def hurwitz_units():
    global _HURWITZ_UNITS
    if _HURWITZ_UNITS is not None:
        return _HURWITZ_UNITS
    units = []
    for i in range(4):
        coords = [0, 0, 0, 0]
        coords[i] = 1
        units.append(HurwitzQuaternion.from_ints(*coords))
        coords[i] = -1
        units.append(HurwitzQuaternion.from_ints(*coords))
    for signs in product((1, -1), repeat=4):
        units.append(HurwitzQuaternion(*signs))
    _HURWITZ_UNITS = units
    return units


def to_lipschitz_representative(q: HurwitzQuaternion):
    for u in hurwitz_units():
        cand = q * u
        if cand.is_lipschitz():
            return cand.as_ints()
    return None


def _sieve_primes(limit):
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i in range(2, limit + 1) if is_p[i]]


def _make_M(n):
    limit = min(30, max(6, n.bit_length()))
    primes = _sieve_primes(limit)
    m = 1
    for pr in primes:
        if pr != 2 and n % pr == 0:
            continue
        m *= pr
    return m


def four_squares_odd(n: int):
    if n == 1:
        return (1, 0, 0, 0)

    bound = max(1000, n ** 2)
    M = _make_M(n)

    while True:
        k = 2 * random.randint(0, bound) + 1
        p = M * n * k - 1

        m = (p + 1) // n
        if gcd(m, n) != 1:
            continue

        s = None
        for _ in range(30):
            u = random.randint(2, p - 2)
            cand = pow(u, (p - 1) // 4, p)
            if (cand * cand) % p == p - 1:
                s = cand
                break
        if s is None:
            continue

        g = gaussian_gcd(GaussianInt(s, 1), GaussianInt(p, 0))
        a, b = g.re, g.im
        if a * a + b * b != p:
            continue

        pi = HurwitzQuaternion.from_ints(a, b, 1, 0)
        beta = HurwitzQuaternion.from_ints(n, 0, 0, 0)
        sigma = quaternion_gcrd(pi, beta)

        if sigma.norm() != n:
            continue

        result = to_lipschitz_representative(sigma)
        if result is None:
            continue

        aa, bb, cc, dd = result
        if aa * aa + bb * bb + cc * cc + dd * dd == n:
            return (aa, bb, cc, dd)


def four_squares(n: int):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return (0, 0, 0, 0)

    while True:
        m, mult = n, 1
        while m % 4 == 0:
            m //= 4
            mult *= 2

        if m % 2 == 0:
            half = m // 2
            a, b, c, d = four_squares_odd(half)
            res = (a + b, a - b, c + d, c - d)
        else:
            res = four_squares_odd(m)

        res = tuple(v * mult for v in res)
        if sum(v * v for v in res) == n:
            return res


t = int(input())
for _ in range(t):
    random.seed(time.time_ns())
    n = int(input())
    print(*[abs(v) for v in four_squares(n)])