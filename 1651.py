n, q = map(int, input().split())
a = list(map(int, input().split()))

class SegmentTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n *= 2
        self.tree = [0] * (2 * self.n)
 
    def query(self, i, x):
        i += self.n
        result = self.tree[i]
        i //= 2
        while i >= 1:
            result += self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2
 
    def upd(self, l, r, val):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = min(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2



diff = [a[i] - a[i - 1] for i in range(1, n)]
print(diff)
intervals = []
cached = {}
for _ in range(q):
    r = list(map(int, input().split()))
    if r[0] == 1:
        intervals.append((r[1] - 1, r[2] - 1, r[3]))
        cached = {}
    else:
        k = r[1] - 1
        if k in cached:
            print(cached[k])
        else:
            v = a[k]
            for interval in intervals:
                if interval[0] <= k <= interval[1]:
                    v += interval[2]
            cached[k] = v
            print(v)