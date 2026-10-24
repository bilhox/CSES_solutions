import sys
t = int(input())
result = []
for line in sys.stdin:
    y, x = map(int, line.split())

    if x < y:
        d = y * (1 + 1 + 2 * (y - 1)) // 2
        if y % 2:
            d -= 1 + 2 * (y - 1)
            result.append(str(d + x))
        else:
            result.append(str(d - x + 1))
    else:
        d = x * (1 + 1 + 2 * (x - 1)) // 2
        if x % 2 == 0:
            d -= 1 + 2 * (x - 1)
            result.append(str(d + y))
        else:
            result.append(str(d - y + 1))
sys.stdout.write("\n".join(result))