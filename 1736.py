from itertools import accumulate
n, q = map(int, input().split())

pref_acc = list(accumulate(range(1, n + 1)))
pref_acc.append(0)
#print(pref_acc)

class SegTree:

    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.array = [0] * (2 * self.size)
        self.neutral = 0

    def update(self, sx, sy):
        self._update(sx, sy, 0, self.size)
    
    def _update(self, sx, sy, lx, ly):

        stack = [(0, lx, ly)]

        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                # print(nlx, nly, pref_acc[nly - sx - 1] - pref_acc[nlx - sx - 1])
                self.array[nx] += pref_acc[nly - sx - 1] - pref_acc[nlx - sx - 1]
                continue

            if nlx <= sx <= sy <= nly:
                self.array[nx] += pref[sy - 1] - pref[sx - 1]
            elif nlx <= sx <= nly <= sy:
                self.array[nx] += pref[nly - 1] - pref[sx - 1]
            elif sx <= nlx <= sy <= nly:
                self.array[nx] += pref[sy - 1] - pref[nlx - 1]

            m = (nlx + nly) // 2

            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 1, nlx, m))
                stack.append((2 * nx + 2, m, nly))
    
    def query(self, l, r):
        return self._query(l, r, 0, self.size)

    def _query(self, sx, sy, lx, ly):

        stack = [(0, lx, ly)]
        current = 0

        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue

            
            if sx <= nlx <= nly <= sy: # Completely inside
                current += self.array[nx]
                continue

            m = (nlx + nly) // 2

            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 1, nlx, m))
                stack.append((2 * nx + 2, m, nly))
        
        return current

t = list(map(int, input().split()))
pref = list(accumulate(t))
pref.append(0)

tree = SegTree(n)

for _ in range(q):
    a, b, c = map(int, input().split())

    if a == 1:
        tree.update(b - 1, c)
    else:
        print(tree.query(b - 1, c), pref[c - 1] - pref[b - 2])