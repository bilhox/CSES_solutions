n, q = map(int, input().split())
a = list(map(int, input().split()))
bij = [0 for _ in range(n + 1)]
for i, v in enumerate(a):
    bij[v] = i

r = 1
for i in range(2, n + 1):
    if bij[i] < bij[i - 1]:
        r += 1

res = [0 for _ in range(q)]

before_x = 0
after_x = 0
before_y = 0
after_y = 0

for i in range(q):

    x, y = map(lambda v : int(v) - 1, input().split())
    nx = a[x]
    ny = a[y]

    before_x = nx > 1 and bij[nx - 1] < bij[nx]
    after_x = nx < n and bij[nx] < bij[nx + 1]
    before_y = ny > 1 and bij[ny - 1] < bij[ny]
    after_y = ny < n and bij[ny] < bij[ny + 1]

    temp = bij[nx]
    bij[nx] = bij[ny]
    bij[ny] = temp

    temp_2 = a[x]
    a[x] = a[y]
    a[y] = temp_2

    before_x -= nx > 1 and bij[nx - 1] < bij[nx]
    after_x -= nx < n and bij[nx] < bij[nx + 1]
    before_y -= ny > 1 and bij[ny - 1] < bij[ny]
    after_y -= ny < n and bij[ny] < bij[ny + 1]
    
    r += after_x
    r += after_y

    if abs(nx - ny) != 1:
        r += before_x
        r += before_y
    elif nx + 1 == ny:
        r += before_x
    else:
        r += before_y

    res[i] = r

for el in res:
    print(el)
