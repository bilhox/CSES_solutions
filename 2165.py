n = int(input())

def hanoi(n, i=1, j=2, k=3):
    if n == 0:
        return
    hanoi(n - 1, i, k, j)
    print(f"{i} {k}")
    hanoi(n - 1, j, i, k)

print(2**n - 1)
hanoi(n)