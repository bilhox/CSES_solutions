t = int(input())

def get_seg_equation(a, b):
    equation = (a[1] - b[1], b[0] - a[0], -(a[1] - b[1])*a[0] - (b[0] - a[0])*a[1])
    
    return equation

tests = [list(map(int, input().split())) for _ in range(t)]

for test in tests:
    ax, ay, bx, by, cx, cy = test

    v1 = (cx - ax, cy - ay)
    v2 = (cx - bx, cy - by)
    
    equation = get_seg_equation((ax, ay), (bx, by))

    val = equation[0] * cx + equation[1] * cy + equation[2]
    if val == 0:
        print("TOUCH")
    elif val < 0:
        print("RIGHT")
    else:
        print("LEFT")