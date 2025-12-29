n = int(input())

def dist_squared(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1]

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

def inter1(a : int, b : int, c : int, d : int):
    a_bis = min(a, b)
    b_bis = max(a, b)
    c_bis = min(c, d)
    d_bis = max(c, d)

    return max(a_bis, c_bis) <= min(b_bis, d_bis)

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def sign(x : int):
    return -1 if x < 0 else int(x > 0)

points = []
for _ in range(n):
    ax, ay = map(int, input().split())
    points.append((ax, ay))

seg = []
for i in range(n):
    seg.append([points[i], points[(i + 1) % n]])

r = 0

for s in seg:
    ax, ay, bx, by = s[0][0], s[0][1], s[1][0], s[1][1]
    r += (ax - bx) * (ay + by)

print(abs(r))