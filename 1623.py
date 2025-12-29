def solve(ind, arr, sum_a, sum_b):
    if ind == len(arr):
        return abs(sum_a - sum_b)

    l1 = solve(ind + 1, arr, sum_a + arr[ind], sum_b)
    l2 = solve(ind + 1, arr, sum_a, sum_b + arr[ind])

    return min(l1, l2)

n = int(input())
l = [int(v) for v in input().split()]

print(solve(0, l, 0, 0))
