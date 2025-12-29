n = int(input())
a = [int(v) for v in input().split()]
a.sort()
v = 1
for el in a:
    if v + 1 <= el:
        print(v)
        exit()
    v += el
print(v)
    