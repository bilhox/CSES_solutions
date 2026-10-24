import sys
buffer = iter(sys.stdin.buffer.read().split())
n, q = int(next(buffer)), int(next(buffer))
a = [0]
a.extend(map(int, (next(buffer) for _ in range(n))))

succ = []
succ.append(a)

for i in range(1, 31):
    l = [succ[-1][succ[-1][j]] for j in range(n + 1)]
    succ.append(l)

# for line in succ:
#     print(line)

results = []

for _ in range(q):
    x, k = int(next(buffer)), int(next(buffer))

    ancestor = x
    for i in range(31):
        if k & (1 << i):
            ancestor = succ[i][ancestor]
    
    results.append(str(ancestor))

sys.stdout.write("\n".join(results) + "\n")