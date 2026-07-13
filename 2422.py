n = int(input())

def check(x):

    total = 0
    for l in range(1, n + 1):
        total += min(n, x // l)
    
    #print(total)
    return total > n**2 // 2

left = 0
right = n**2 + 1
middle = None

while left + 1 < right:
    middle = (left + right) // 2
    #print(left, middle, right)
    if check(middle):
        right = middle
    else:
        left = middle

print(right)