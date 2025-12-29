n = int(input())

check_io = set()
incr = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a not in incr:
        incr[a] = [1, 0]
    else:
        incr[a][0] += 1
    if b not in incr:
        incr[b] = [0, 1]
    else:
        incr[b][1] += 1

    check_io.add(b)
    check_io.add(a)
 
check_io = list(check_io)

check_io.sort()
 
max_v = 0
curr_s = 0
for t in check_io:
    curr_s += incr[t][0]
    max_v = max(max_v, curr_s)
    curr_s -= incr[t][1]
print(max_v)