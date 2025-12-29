t = int(input())

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

for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    a = (x1, y1)
    b = (x2, y2)
    c = (x3, y3)
    d = (x4, y4)

    d1 = sub(b, a)
    d2 = sub(d, c)

    if det(sub(c, a), sub(c, b)) == 0 and det(sub(d, a), sub(d, b)) == 0:
        if inter1(x1, x2, x3, x4) and inter1(y1, y2, y3, y4):
            print("YES")
        else:
            print("NO")
    else:
        if sign(det(sub(b, a), sub(d, a))) != sign(det(sub(b, a), sub(c, a))) and sign(det(sub(d, c), sub(a, c))) != sign(det(sub(d, c), sub(b, c))):
            print("YES")
        else:
            print("NO")