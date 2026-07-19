import sys
from io import IOBase, BytesIO
import os
from heapq import *

# region fastio
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
 
def dijkstra_opt(graph, n, s, k):
 
    dist_shortest = [[] for _ in range(n)]
 
    dist_shortest[s].append(0)
    heap = [(0, s)]
 
    while heap:
        d_v, v = heappop(heap)
        
        if -d_v < dist_shortest[v][0]:
            continue
        #print(v, dist_shortest)
 
        for neigh in graph[v]:
            node, length = neigh
            add = d_v + length
            if len(dist_shortest[node]) < k:
                heappush(dist_shortest[node], -add)
                heappush(heap, (add, node))
            elif -add > dist_shortest[node][0]:
                heappop(dist_shortest[node])
                heappush(dist_shortest[node], -add)
                heappush(heap, (add, node))
    
    return dist_shortest[n - 1]
 
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
 
for line in sys.stdin:
    a, b, c = map(int, line.split())
    graph[a].append((b, c))
 
top = dijkstra_opt(graph, n + 1, 1, k)
print(*sorted([-v for v in top]))