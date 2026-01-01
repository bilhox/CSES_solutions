import sys

flush = sys.stdout.flush

l = 0
r = 10**9 + 1
m = None

def ask(x):
    print(f"? {x}")
    flush()
    ans = input()
    return ans == "YES"

while l + 1 < r:
    m = (l + r) // 2
    ans = ask(m)
    if ans:
        l = m
    else:
        r = m

print(f"! {r}")