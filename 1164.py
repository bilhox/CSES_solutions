from collections import deque

n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((i, a, -1))
    s.append((i, b, 1))

s.sort(key=lambda v : v[1])

assigned = [0 for _ in range(n)]
available = deque([(1, 0)])
room_index = 1
for check in s:
    a, b, c = check
    if c == -1:
        if len(available) == 0:
            room_index += 1
            available.append((room_index, 0))
        else:
            room = available.pop()
            available.append(room)
            if room[1] == b:
                room_index += 1
                available.append((room_index, 0))
            
        assigned[a] = available.pop()[0]
    else:
        available.appendleft((assigned[a], b))

print(room_index)
print(*assigned)
