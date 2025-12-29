import bisect

n = int(input())
cubes = list(map(int, input().split()))
last_seen = []
for value in cubes:
    if not last_seen:
        last_seen.append(value)
        continue
    else:
        ind = bisect.bisect_right(last_seen, value)
        if ind == len(last_seen):
            last_seen.append(value)
        else:
            last_seen[ind] = value
    

print(len(last_seen))