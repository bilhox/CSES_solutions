q = int(input())

def query():
    a, b = map(int, input().split())
    removed_so_far = 0
    first = 1
    remove_first = False
    k = 2
    while removed_so_far < a:
        rem = a - removed_so_far
        removed = rem // 2
        if remove_first:
            removed += (rem % 2) * remove_first
            

        removed_so_far += removed
        if removed_so_far >= b:
            removed_so_far -= removed
            diff = b - removed_so_far - 1
            if remove_first:
                return first + diff * k
            else:
                return first + k // 2 + diff * k
        
        if remove_first:
            first += k // 2

        if (rem % 2) == (not remove_first):
            remove_first = True
        else:
            remove_first = False

        k <<= 1



for _ in range(q):
    print(query())



"""
1 2 3 4 5 6 7 8 9 10 11
1 X 3 X 5 X 7 X 9 XX 11
X X 3 X X X 7 X X XX 11
X X X X X X 7 X X XX XX
X X X X X X X X X XX XX
"""