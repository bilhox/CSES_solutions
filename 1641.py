n, x = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    for i in range(n):
        seen = {}
        for j in range(i, n):
            if i == j:
                continue
            if a[j] not in seen:
                seen[x - a[j] - a[i]] = j + 1
            else:
                return [i + 1, seen[a[j]], j + 1]
    
    return "IMPOSSIBLE"

verdict = solve()
if isinstance(verdict, list):
    print(*verdict)
else:
    print(verdict)
