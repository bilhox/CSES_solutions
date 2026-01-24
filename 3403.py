n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def lcs():

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            equals = b[i - 1] == a[j - 1]
            if equals:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # for line in dp:
    #     print(*[len(v) for v in line])

    res = dp[-1][-1]
    ptr_x = n
    ptr_y = m
    lcs_seq = []
    while dp[ptr_y][ptr_x] != 0:

        if b[ptr_y - 1] == a[ptr_x - 1]:
            lcs_seq.append(a[ptr_x - 1])
            ptr_x -= 1
            ptr_y -= 1
        elif dp[ptr_y][ptr_x - 1] > dp[ptr_y - 1][ptr_x]:
            ptr_x -= 1
        else:
            ptr_y -= 1
    
    return res, lcs_seq[::-1]

length, seq = lcs()
print(length)
print(*seq)