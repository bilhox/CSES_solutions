n = int(input())
d = {}
c = 0
for a in input().split():
    if a not in d:
        d[a] = True
        c += 1

print(c)