
n, t = map(int, input().split())
k = list(map(int, input().split()))
k.sort()

def check(x):
    
    count = 0
    for v in k:
        count += x // v
        if count >= t:
            return True
    
    return False

def dicho():

    left = -1
    right = max(k) * t + 1
    middle = None

    while left + 1 < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle
    
    return right

print(dicho())