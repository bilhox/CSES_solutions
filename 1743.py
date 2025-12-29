s = input()
n = len(s)
count = [0 for _ in range(26)]
res = ["" for _ in range(n)]
c = -1

for ch in s: count[ord(ch) - ord('A')] += 1

if not all(2 * v <= (n + 1) for v in count):
    print(-1)
    exit()

for i in range(n):
    found = False
    for j in range(26):
        char = chr(ord('A') + j)
        if count[j] == 0:
            continue
        if c != -1 and res[c] == char:
            continue
        count[j] -= 1
        is_valid = 2 * max(count) <= n - i
        if is_valid:
            res[i] = char
            found = True
            c += 1
            break
        count[j] += 1
    if not found:
        print(-1)
        exit()

print("".join(res))

