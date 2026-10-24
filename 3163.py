class SegTree:
 
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.array_min = [10**18] * (2 * self.size)
 
    def update(self, sx, sy, v):
        stack = [(0, 0, self.size)]
 
        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                self.array_min[nx] = min(self.array_min[nx], v)
                # print(current_value, self.array[nx])
                continue
 
            m = (nlx + nly) // 2
 
            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 2, m, nly))
                stack.append((2 * nx + 1, nlx, m))
        
    
    def query(self, i):
        stack = [(0, 0, self.size)]
        current_min = 10**18
 
        while stack:
            nx , nlx, nly = stack.pop()

            current_min = min(current_min, self.array_min[nx])
 
            if nly - nlx == 1:
                return current_min
            
            m = (nlx + nly) // 2

            if i < m:
                stack.append((2 * nx + 1, nlx, m))
            else:
                stack.append((2 * nx + 2, m, nly))

        return current_min


n, q = map(int, input().split())
x = list(map(int, input().split()))
starts1 = [0] * n
ends1 = [0] * n
events2 = []

tree = SegTree(n)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    starts1[a - 1] += 1
    ends1[b - 1] += 1
    tree.update(a - 1, b, d)

total = 0
opened_so_far = 0
for i in range(n):
    l = starts1[i]
    r = ends1[i]

    opened_so_far += l
    m
