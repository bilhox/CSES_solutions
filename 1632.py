from collections import deque


n, k = map(int, input().split())
 
movies = []
for i in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))
 
movies.sort(key=lambda u : u[1])

watched = 0
watching = deque([])

print(movies)

# a = [(57, 69), (35, 72)]
# b = deque([])
# b.extend(a)
# print(b)

"""
Does not work as deque.extendleft doesn't do what I imagined it should do
"""

for movie in movies:

    popped = []
    while watching:
        temp_movie = watching.popleft()
        if temp_movie[1] <= movie[0]:
            watching.extendleft(popped)
            break
        popped.append(temp_movie)
    else:
        watching.extendleft(popped)

    if len(watching) < k:
        watched += 1
        watching.appendleft(movie)
    
    print(watching)

print(watched)