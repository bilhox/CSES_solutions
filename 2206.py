import sys
 
class LeftSegTree:
 
    def __init__(self, n : int):
        self.size = (1 << n.bit_length())
        if n.bit_count() == 1 and (n >> (n.bit_length() - 1)) & 1:
            self.size >>= 1
        
        self.array1 = [10**18] * (2 * self.size)
        self.array2 = [1] * (2 * self.size)
 
    def build(self, array):
 
        for i in range(len(array)):
            self.array1[self.size - 1 + i] = array[i]
            self.array2[self.size - 1 + i] = 1
 
        for i in range(self.size - 2, -1, -1):
            u0, u1 = self.array1[2 * i + 1], self.array2[2 * i + 1]
            v0, v1 = self.array1[2 * i + 2], self.array2[2 * i + 2]
            self.array1[i] = min(v0 + u1, u0)
            self.array2[i] = u1 + v1
 
        # print(self.array1)
        # print(self.array2)
 
    def query(self, sx, sy):
        stack = [(0, 0, self.size)]
        c0 = 10**18
        c1 = 0
 
        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                v0, v1 = self.array1[nx], self.array2[nx]
                c0 = min(v0 + c1, c0)
                c1 += v1
                continue
 
            m = (nlx + nly) // 2
 
            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 2, m, nly))
                stack.append((2 * nx + 1, nlx, m))
        
        return c0
    
    def update(self, val, i):
        stack = [(0, 0, self.size, False)]
 
        while stack:
            nx , nlx, nly, computable = stack.pop()
 
            if nly - nlx == 1:
                self.array1[nx] = val
                continue
            
            if not computable:
                stack.append((nx, nlx, nly, True))
                m = (nlx + nly) // 2
 
                if i < m:
                    stack.append((2 * nx + 1, nlx, m, False))
                else:
                    stack.append((2 * nx + 2, m, nly, False))
            else:
                u0, u1 = self.array1[2 * nx + 1], self.array2[2 * nx + 1]
                v0 = self.array1[2 * nx + 2]
                self.array1[nx] = min(v0 + u1, u0)
 
class RightSegTree:
 
    def __init__(self, n : int):
        self.size = (1 << n.bit_length())
        if n.bit_count() == 1 and (n >> (n.bit_length() - 1)) & 1:
            self.size >>= 1
        
        self.array1 = [10**18] * (2 * self.size)
        self.array2 = [1] * (2 * self.size)
 
    def build(self, array):
 
        for i in range(len(array)):
            self.array1[self.size - 1 + i] = array[i]
            self.array2[self.size - 1 + i] = 1
 
        for i in range(self.size - 2, -1, -1):
            u0, u1 = self.array1[2 * i + 1], self.array2[2 * i + 1]
            v0, v1 = self.array1[2 * i + 2], self.array2[2 * i + 2]
            self.array1[i] = min(u0 + v1, v0)
            self.array2[i] = u1 + v1
 
        # print(self.array1)
        # print(self.array2)
 
    def query(self, sx, sy):
        stack = [(0, 0, self.size)]
        c0 = 10**18
        c1 = 0
 
        while stack:
            nx, nlx, nly = stack.pop()
        
            if nly < sx or nlx >= sy: # Completely outside
                continue
            
            if sx <= nlx <= nly <= sy: # Completely inside
                v0, v1 = self.array1[nx], self.array2[nx]
                c0 = min(c0 + v1, v0)
                c1 += v1
                continue
 
            m = (nlx + nly) // 2
 
            if sy < m:
                stack.append((2 * nx + 1, nlx, m))
            elif sx >= m:
                stack.append((2 * nx + 2, m, nly))
            else:
                stack.append((2 * nx + 2, m, nly))
                stack.append((2 * nx + 1, nlx, m))
        
        return c0
    
    def update(self, val, i):
        stack = [(0, 0, self.size, False)]
 
        while stack:
            nx , nlx, nly, computable = stack.pop()
 
            if nly - nlx == 1:
                self.array1[nx] = val
                continue
            
            if not computable:
                stack.append((nx, nlx, nly, True))
                m = (nlx + nly) // 2
 
                if i < m:
                    stack.append((2 * nx + 1, nlx, m, False))
                else:
                    stack.append((2 * nx + 2, m, nly, False))
            else:
                u0 = self.array1[2 * nx + 1]
                v0, v1 = self.array1[2 * nx + 2], self.array2[2 * nx + 2]
                self.array1[nx] = min(u0 + v1, v0)
 
n, q = map(int, input().split())
p = list(map(int, input().split()))
 
tree1 = LeftSegTree(n)
tree2 = RightSegTree(n)
 
tree1.build(p)
tree2.build(p)
output = []
for line in sys.stdin:
    u = list(map(int, line.split()))
    if u[0] == 2:
        k = u[1]
        output.append(str(min(tree2.query(0, k), tree1.query(k - 1, n))))
    else:
        k, x = u[1], u[2]
        tree1.update(x, k - 1)
        tree2.update(x, k - 1)

sys.stdout.write("\n".join(output))