from collections import defaultdict
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
left = 0
right = 0
last_boundary = -1
 
total = 0
count = defaultdict(int)
 
while(right < n):
    count[a[right]] += 1
    if len(count) > k:
        extra = ((last_boundary - left + 1) * (last_boundary - left + 2)) // 2
        total += ((right - left) * (right - left + 1)) // 2 - extra
        while(len(count) > k):
            count[a[left]] -= 1
            if count[a[left]] == 0:
                del count[a[left]]
            left += 1
        last_boundary = right - 1
    right += 1
 
right -= 1
 
extra = ((last_boundary - left + 1) * (last_boundary - left + 2)) // 2
total += ((right - left + 1) * (right - left + 2)) // 2 - extra
 
print(total)