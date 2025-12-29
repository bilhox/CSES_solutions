n = int(input())
values = list(map(int, input().split()))
last_seen = {}
l = 0
r = 0
max_seg = 0
while r < n:
    if values[r] in last_seen:
        max_seg = max(max_seg, r - l)
        if l <= last_seen[values[r]]:
            l = last_seen[values[r]] + 1

    last_seen[values[r]] = r
    
    r += 1

max_seg = max(max_seg, r - l)
print(max_seg)
