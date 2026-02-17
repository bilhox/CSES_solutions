from itertools import accumulate

n, l, r = map(int, input().split())
a = list(map(int, input().split()))

pref = [0] + list(accumulate(a))

right = n
left = n - r

best_so_far = -float("inf")

stack = []

while right >= l:
    finished = False
    while not finished:
        finished = True
        if not stack:
            continue
        if right - stack[-1][0] < l:
            stack.pop()
            finished = False

    if not stack:
        for i in range(right - l, left - 1, -1):
            if not stack:
                stack.append((i, pref[i]))
            elif stack[-1][1] >= pref[i]:
                stack.append((i, pref[i]))

    best_so_far = max(pref[right] - stack[-1][1], best_so_far)

    right -= 1
    left = max(left - 1, 0)

    if stack[-1][1] >= pref[left]:
        stack.append((left, pref[left]))

print(best_so_far)