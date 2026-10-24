t = int(input())

result = []

for _ in range(t):
    n, k = map(int, input().split())

    s = input()
    a = list(map(int, input().split()))

    S = [c == "B" for c in s]

    def check(x):
        color = [0] * n
        used = 0
        for i in range(n):
            if a[i] > x and S[i]:
                color[i] = 1
                used += 1

        last_unset = None
        for i in range(n):
            if last_unset is None:
                if color[i] == 1:
                    last_unset = i
                continue
            if color[i]:
                used -= 1
            elif a[i] > x:
                last_unset = None

        return used <= k

    left = -1
    right = max(a) + 1
    middle = None
    while left + 1 < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle

    result.append(right)

print(*result, sep="\n")