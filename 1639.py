from sys import setrecursionlimit

setrecursionlimit(10000)

a = input().strip()
b = input().strip()

# recursive
def lev_distance(sa, sb):
    dp = [[-1] * (len(a) + 1) for _ in range(len(b) + 1)]
    
    if dp[sb][sa] != -1:
        return dp[sb][sa]
    
    if sa == len(a):
        dp[sb][sa] = len(b) - sb
    elif sb == len(b):
        dp[sb][sa] = len(a) - sa
    elif a[sa] == b[sb]:
        dp[sb][sa] = lev_distance(sa + 1, sb + 1)
    else:
        dp[sb][sa] = 1 + min(
            lev_distance(sa + 1, sb),
            lev_distance(sa, sb + 1),
            lev_distance(sa + 1, sb + 1)
        )

    return dp[sb][sa]

def lev_iterative():

    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

    for i in range(1, len(a) + 1):
        dp[0][i] = i
    
    for i in range(1, len(b) + 1):
        dp[i][0] = i

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            sub = a[j - 1] != b[i - 1]
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + sub
            )
    
    # for line in dp:
    #     print(*line)

    return dp[-1][-1]

print(lev_iterative())