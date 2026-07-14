from heapq import *
import sys
    
n, m = map(int, input().split())
edges = []
heap = []
for i in range(m):
    a, b, c = map(int, next(sys.stdin).split())
    heap.append((c, i))
    edges.append((a - 1, b - 1))

heap.sort(reverse=True)
parents = list(range(n))
rank = [0] * n

def is_one_alone():
    e0 = find(0)
    return any(find(k) != e0 for k in range(n))
    
def find(e):

    if not (0 <= e < n):
        return None

    if parents[e] != e:
        parents[e] = find(parents[e])
    
    return parents[e]

def union(e1, e2):

    r1, r2 = find(e1), find(e2)
    if r1 == r2:
        return
    
    if rank[r1] < rank[r2]:
        r1, r2 = r2, r1
    
    parents[r2] = r1

    if rank[r1] == rank[r2]:
        rank[r1] += 1
    

def is_same_set(e1, e2):
    return find(e1) == find(e2)


total_cost = 0
while heap:
    c, i = heap.pop()
    a, b = edges[i]
    if is_same_set(a, b):
        continue
    total_cost += c
    union(a, b)

if not is_one_alone():
    print(total_cost)
else:
    print("IMPOSSIBLE")