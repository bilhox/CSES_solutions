from bisect import *
from collections import defaultdict, Counter
X = 181938374921
n, x = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    print(int(x == a[0]))
    exit()

def get_subset_sums(l: int, r: int) -> Counter:
	sums = [0]
	for ti in a[l:r]:
		sums.extend([s + ti for s in sums])
	return Counter(sums)

count = 0
# partial_sums1 = [0] * (1 << (n // 2))
# partial_sums2 = [0] * (1 << ((n + 1) // 2))

# for bitset in range(1 << (n // 2)):

#     s = 0
#     for j in range(n // 2):
#         if (bitset >> j) & 1:
#             s += a[j]
    
#     partial_sums1[bitset] = s

# for bitset in range(1 << ((n + 1) // 2)):

#     s = 0
#     for j in range(n // 2, n):
#         if (bitset >> (j - n // 2)) & 1:
#             s += a[j]
    
#     partial_sums2[bitset] = s


count1 = get_subset_sums(0, n // 2)
count2 = get_subset_sums(n // 2, n)

for v in count1:
    count += count1[v] * count2.get(x - v, 0)

print(count)