n = int(input())
a = [k for k in range(1, n + 1)]
removed = []
lastly_removed = True
while len(removed) != n:
    for i in range(n):
        if a[i] == -1:
            continue
        if not lastly_removed:
            removed.append(a[i])
            a[i] = -1
        lastly_removed = not lastly_removed
 
print(*removed)