
s = input().strip()
visited = [[False for _ in range(7)] for _ in range(7)]
visited[0][0] = True
N = 7

direc = {"L":(-1, 0), "R":(1, 0), "U":(0, -1), "D":(0, 1)}
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# stack = [(0, 0, 0)]
res = 0

# while stack:
#     x, y, count = stack.pop()
#     if count == N**2 - 1:
#         res += (x == 0 and y == N - 1)
#         continue

#     if s[count] != "?":
#         vec = direc[s[count]]
#         cx = x + vec[0]
#         cy = y + vec[1]
#         if not (0 <= cx <= N - 1) or not (0 <= cy <= N - 1) or visited[cy][cx]:
#             continue
        
#         stack.append((cx, cy, count + 1))
    


def find_paths(x, y, count):
    global res
    if count == N**2 - 1:
        res += (x == 0 and y == N - 1)
        return

    if s[count] != "?":
        vec = direc[s[count]]
        cx = x + vec[0]
        cy = y + vec[1]
        if (0 <= cx <= N - 1) and (0 <= cy <= N - 1) and not visited[cy][cx]:
            visited[cy][cx] = True
            find_paths(cx, cy, count + 1)
            visited[cy][cx] = False
        return
    blocked = [False] * 4
    indices = []
    for i in range(4):
        cx = x + moves[i][0]
        cy = y + moves[i][1]
        if not (0 <= cx <= N - 1) or not (0 <= cy <= N - 1) or visited[cy][cx]:
            blocked[i] = True
        else:
            indices.append(i)
    
    if blocked[2] and blocked[3] and not blocked[0] and not blocked[1]:
        return
    if blocked[0] and blocked[1] and not blocked[2] and not blocked[3]:
        return

    for i in indices:
        if blocked[i]:
            continue
        cx = x + moves[i][0]
        cy = y + moves[i][1]
        visited[cy][cx] = True
        find_paths(cx, cy, count + 1)
        visited[cy][cx] = False

find_paths(0, 0, 0)
print(res)