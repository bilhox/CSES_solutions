from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

s = input()
@bootstrap
def find_paths(x, y, count, visited, n, path):
    if count == n**2 - 1:
        yield (x == 0 and y == n - 1)
 
    if path[count] != "?":
        direc = {"L":(-1, 0), "R":(1, 0), "U":(0, -1), "D":(0, 1)}
        vec = direc[path[count]]
        cx = x + vec[0]
        cy = y + vec[1]
        if not (0 <= cx <= n - 1) or not (0 <= cy <= n - 1) or visited[cy][cx]:
            yield 0
        else:
            visited[cy][cx] = True
            r = next(find_paths(cx, cy, count + 1, visited, n, path))
            visited[cy][cx] = False
            yield r
    blocked = [False, False, False, False]
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i, move in enumerate(moves):
        cx = x + move[0]
        cy = y + move[1]
        if not (0 <= cx <= n - 1) or not (0 <= cy <= n - 1) or visited[cy][cx]:
            blocked[i] = True
    
    if (blocked[2] and blocked[3]) and not blocked[0] and not blocked[1]:
        yield 0
    if (blocked[0] and blocked[1]) and not blocked[2] and not blocked[3]:
        yield 0
    
    res = 0
 
    for i, move in enumerate(moves):
        cx = x + move[0]
        cy = y + move[1]
        if blocked[i]:
            continue
        visited[cy][cx] = True
        res += next(find_paths(cx, cy, count + 1, visited, n, path))
        visited[cy][cx] = False
    yield res
 
 
visited = [[False for _ in range(7)] for _ in range(7)]
visited[0][0] = True
n = find_paths(0, 0, 0, visited, 7, s)
print(n)