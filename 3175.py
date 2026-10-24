from collections import deque
n = int(input())

numbers = [0] * (n + 1)
p = []

while numbers:
    if not p:
        p.append(numbers.pop())
        continue

    current = p[-1]
    u = numbers.pop()
    temp = []
    no_solution = False
    while abs(current - u) == 1:
        temp.append(u)
        if not numbers:
            no_solution = True
            break
        u = numbers.pop()
    
    if not no_solution:
        p.append(u)
        for v in temp:
            numbers.append(v)
        continue

    numbers.extend(temp)
    finished = False
    while not finished:
        if not p:
            print("NO SOLUTION")
            exit()
        v = p.pop()
        if v == n:
            numbers.append(v)
            continue



print(*p)
