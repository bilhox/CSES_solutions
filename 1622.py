from collections import Counter
s = input()
s = sorted(s)

def foo(n, s, count, dp):
    if n == 1:
        return set(s)
    else:
        res = foo(n - 1, s, count, dp)
        return set(c + a for a in res for c in s if a.count(c) < count[c])

r = sorted(foo(len(s), s, Counter(s), {}))
print(len(r))
print(*r, sep='\n')