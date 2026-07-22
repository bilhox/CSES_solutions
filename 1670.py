from collections import deque
l1, l2, l3 = input().split(), input().split(), input().split()
l1 = [int(v) for v in l1]
l2 = [int(v) for v in l2]
l3 = [int(v) for v in l3]
inp = [l1, l2, l3]

def get_state(u):

    state = 0
    for i in range(9):
        v = u[i // 3][i % 3]
        state += v << (4 * i)
    
    return state

target = get_state([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

visited = {get_state(inp)}
queue = deque([(get_state(inp), 0)])
result = 0
while queue:
    state, dist = queue.pop()

    if state == target:
        result = dist
        break

    for i in range(9):
        if i % 3 != 2:
            lstate = state
            a = (lstate >> (4 * i)) & 15
            b = (lstate >> (4 * i + 4)) & 15
            lstate ^= a << (4 * i)
            lstate ^= b << (4 * i + 4)
            lstate ^= a << (4 * i + 4)
            lstate ^= b << (4 * i)
            if lstate not in visited:
                visited.add(lstate)
                queue.appendleft((lstate, dist + 1))
        if i < 6:
            rstate = state
            a = (rstate >> (4 * i)) & 15
            b = (rstate >> (4 * (i + 3))) & 15
            rstate ^= a << (4 * i)
            rstate ^= b << (4 * (i + 3))
            rstate ^= a << (4 * (i + 3))
            rstate ^= b << (4 * i)
            if rstate not in visited:
                visited.add(rstate)
                queue.appendleft((rstate, dist + 1))

print(result)