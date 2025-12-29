from collections import deque

n = int(input())
movies_times = []
for i in range(n):
    a, b = map(int, input().split())
    movies_times.append((a, b))

movies_times.sort(key=lambda v: v[1])
current_movie = None
curr_v = 0

for movie_time in movies_times:
    a, b = movie_time
    if current_movie == None or current_movie[1] <= a or current_movie[0] >= b:
        curr_v += 1
        current_movie = movie_time

print(curr_v)
