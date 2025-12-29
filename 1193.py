n, m = map(int, input().split())

from queue import Queue

def parse_path(l, pos_1, pos_2):

    W = len(l[0])
    H = len(l)

    s = []
    x = pos_2[0]
    y = pos_2[1]

    while x != pos_1[0] or y != pos_1[1]:
        next_pos = l[y][x]

        cx, cy = next_pos[0] - x, next_pos[1] - y
        if cx == -1:
            s.append("R")
        elif cx == 1:
            s.append("L")
        elif cy == 1:
            s.append("U")
        else:
            s.append("D")

        x = next_pos[0]
        y = next_pos[1]

    return "".join(s)[::-1]

def bfs(lab, pos_1, pos_2):

    W = len(lab[0])
    H = len(lab)

    visited = [[False for _ in range(W)] for _ in range(H)]
    path = [[(-1, -1) for _ in range(W)] for _ in range(H)]

    queue = Queue()
    queue.put([pos_1[0], pos_1[1], -1, -1])
    visited[pos_1[1]][pos_1[0]] = True

    while not queue.empty():
        x, y, px, py = queue.get()
        path[y][x] = (px, py)
        if x == pos_2[0] and y == pos_2[1]:
            return parse_path(path, pos_1, pos_2)

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            cx = max(0, min(x + dx, W - 1))
            cy = max(0, min(y + dy, H - 1))
            if not visited[cy][cx] and lab[cy][cx] != '#' or lab[cy][cx] == "B":
                queue.put((cx, cy, x, y))
                visited[cy][cx] = True
    
    return ""

lab = [input() for _ in range(n)]
pos_1 = None
pos_2 = None
for j in range(n):
    if "A" in lab[j]:
        pos_1 = [lab[j].index("A"), j]
    if "B" in lab[j]:
        pos_2 = [lab[j].index("B"), j]

result = bfs(lab, pos_1, pos_2)
if result != "":
    print("YES")
    print(len(result))
    print(result)
else:
    print("NO")