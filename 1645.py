n = int(input())
a = list(map(int, input().split()))

stack = []
result = [0] * n

for i in range(n):
    if not stack:
        stack.append(i)
        continue
    
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    else:
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

print(*result)
