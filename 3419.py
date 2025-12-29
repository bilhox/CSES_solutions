from math import inf
n = int(input())

actual_grid = [[0] * n for _ in range(n)]

for i in range(n):
    actual_grid[i][0] = actual_grid[0][i] = i

for i in range(1, n):
    for j in range(i + 1, n):

        mex = inf

        v_set = set()

        for k in range(j):
            v_set.add(actual_grid[i][k])
        
        for k in range(i):
            v_set.add(actual_grid[k][j])
        
        for k in range(2 * n):
            if k not in v_set:
                mex = k
                break
        
        actual_grid[i][j] = actual_grid[j][i] = mex

for line in actual_grid:
    print(*line)