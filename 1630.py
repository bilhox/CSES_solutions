n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]

tasks.sort(key=lambda u : u[0])

score = 0
when = 0
for task in tasks:
    duration, deadline = task
    when += duration
    score += deadline - when

print(score)