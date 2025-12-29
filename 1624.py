chessboard = [input() for _ in range(8)]

def solve(chessboard, row, dp, ds, columns, ans):
    if row == 8:
        ans[0] += 1
        return

    for i in range(8):
        if chessboard[row][i] == "*" or columns[i] or dp[7 + row - i] or ds[row + i]:
            continue
        
        columns[i] = True
        dp[7 + row - i] = True
        ds[row + i] = True
        solve(chessboard, row + 1, dp, ds, columns, ans)
        columns[i] = False
        dp[7 + row - i] = False
        ds[row + i] = False

dp = [False for _ in range(16)]
ds = [False for _ in range(16)]
columns = [False for _ in range(10)]

ans = [0]
solve(chessboard, 0, dp, ds, columns, ans)
print(ans[0])