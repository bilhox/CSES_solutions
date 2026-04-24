n = int(input())
total = 0
"""
0000
0001
0010
0011
0100
0101
0110
0111
"""

for i in range(65):
    count = (n + 1) // 2**i
    if count % 2:
        total += (n + 1) % 2**i
    total += (count // 2) * 2**i

print(total)