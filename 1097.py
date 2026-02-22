from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**5)

n = int(input())
x = list(map(int, input().split()))

def recursive_solution(turn, l, r, dp=None):

    if dp is None:
        dp = {}
    
    if (l, r) in dp:
        return dp[(l, r)]
    
    if r < l:
        return (0, 0)
    
    a1 = recursive_solution(not turn, l + 1, r)
    a2 = recursive_solution(not turn, l, r - 1)
    result = (0, 0)

    if turn:
        if x[l] + a1[0] < x[r] + a2[0]:
            result = (x[r] + a2[0], a2[1])
        else:
            result = (x[l] + a1[0], a1[1])
    else:
        if x[l] + a1[1] < x[r] + a2[1]:
            result = (a2[0], x[r] + a2[1])
        else:
            result = (a1[0], x[l] + a1[1])

    dp[(l, r)] = result

    return dp[(l, r)]

def iterative_solution():

    dp = [[0] * 2 for _ in range(n)]

    turn = n % 2

    for i in range(n):
        if turn:
            dp[i][0] = x[i]
        else:
            dp[i][1] = x[i]

    for i in range(1, n):
        turn = not turn
        for j in range(n - i):
            if turn:
                if dp[j][0] + x[j + i] < dp[j + 1][0] + x[j]:
                    dp[j][1] = dp[j + 1][1]
                    dp[j][0] = dp[j + 1][0] + x[j]
                else:
                    dp[j][1] = dp[j][1]
                    dp[j][0] = dp[j][0] + x[j + i]
            else:
                if dp[j][1] + x[j + i] < dp[j + 1][1] + x[j]:
                    dp[j][0] = dp[j + 1][0]
                    dp[j][1] = dp[j + 1][1] + x[j]
                else:
                    dp[j][0] = dp[j][0]
                    dp[j][1] = dp[j][1] + x[j + i]

    return dp[0][0]

print(iterative_solution())