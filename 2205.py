n = int(input())

def get_list(n):
    if n == 1:
        return ["0", "1"]
    else:
        res = get_list(n - 1)
        return ["0" + el for el in res] + ["1" + el for el in res[::-1]]

print(*get_list(n), sep="\n")