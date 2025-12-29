from collections import deque

n, k = map(int, input().split())
 
movies = []
incr = {}
for i in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))
 
movies.sort(key=lambda u : u[1])

watched = 0
watching = deque([])
movies_watched = []

# print(movies)

for movie in movies:

    if len(watching) == k:
        temp = watching[-1]
        if temp[1] <= movie[0]:

            popped = []
            while watching:
                temp_movie = watching.popleft()
                if temp_movie[1] <= movie[0]:
                    watching.extendleft(popped)
                    break
                popped.append(temp_movie)

    if len(watching) < k:
        watched += 1
        watching.appendleft(movie)

print(watched)