import sys

def test_query(i, j):
    L = [1, 6, 3, 2, 8, 5, 4, 7]
    return "YES" if L[i] < L[j] else "NO"

def query(i, j):
    print(f"? {i} {j}")
    sys.stdout.flush()
    verdict = input()
    return verdict

n = int(input())
inversions = [0] * n

for i in range(n - 1, -1, -1):
    for j in range(i):
        if query(i + 1, j + 1) == "YES":
            inversions[i] += 1

cand = [1] * n
p = [0] * n
for i in range(n - 1, -1, -1):
    cursor = n
    count = 0
    while count <= inversions[i]:
        cursor -= 1
        if cand[cursor]:
            count += 1
    cand[cursor] = 0
    p[i] = cursor + 1

print("!", *p)