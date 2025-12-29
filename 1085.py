n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
    current_sum = 0
    counter = 0
    for v in a:
        current_sum += v
        if current_sum >= x:
            counter += 1
            current_sum = 0 if current_sum == x else v
            if current_sum > x:
                return False
    
    if current_sum > 0:
        counter += 1

    return counter <= k

result = [10**18]

def dicho(a, l, r, k, res=result):

    if l + 1 >= r:
        return

    m = (l + r) // 2
    if check(m):
        res[0] = m
        dicho(a, l, m, k)
    else:
        dicho(a, m, r, k)


dicho(a, -1, 10**18, k)
print(result[0])