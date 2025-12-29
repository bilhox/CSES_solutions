n = int(input())
t = list(map(int, input().split()))
t.sort()
time_taken_1 = 0
time_taken_2 = 0

left = 0
right = n - 1

left_boundary = 0
skipped = None

while left < n and right >= left_boundary:
    next_a = t[left]
    if left != right:
        time_taken_1 += next_a
        left += 1
        while time_taken_1 - time_taken_2 >= t[right]:
            time_taken_2 += t[right]
            right -= 1
    elif left != n - 1:
        skipped = left
        left += 1
    else:
        time_taken_2 += t[right]
        time_taken_1 += time_taken_2 - time_taken_1
        right -= 1

if skipped != None:
    time_taken_1 += t[skipped]    

while left < n:
    time_taken_1 += t[left]
    left += 1

while right >= 0:
    time_taken_2 += t[right]
    right -= 1

print(max(time_taken_1, time_taken_2))