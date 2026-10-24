t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    for x in map(int, input().split()):
        total ^= (x % 4)
    
    if total == 0:
        print("second")
    else:
        print("first")