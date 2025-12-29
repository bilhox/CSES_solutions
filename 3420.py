from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

left = 0
right = 0
last_boundary = -1

total = 0
count = defaultdict(int)

while(right < n):
    count[a[right]] += 1
    if count[a[right]] > 1:
        extra = ((last_boundary - left + 1) * (last_boundary - left + 2)) // 2
        total += ((right - left) * (right - left + 1)) // 2 - extra
        while(count[a[right]] != 1):
            count[a[left]] -= 1
            left += 1
        last_boundary = right - 1
    right += 1

right -= 1

extra = ((last_boundary - left + 1) * (last_boundary - left + 2)) // 2
total += ((right - left + 1) * (right - left + 2)) // 2 - extra

print(total)