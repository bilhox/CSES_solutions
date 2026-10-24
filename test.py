from itertools import permutations
s = input()
result = []
for u in permutations(list(s)):
  result.append("".join(u))

print(*set(result), sep="\n")