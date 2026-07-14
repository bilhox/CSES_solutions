from heapq import *
import sys
    
n, m = map(int, input().split())
edges = []
counts = [1] * n
for i in range(m):
    a, b = map(int, next(sys.stdin).split())
    edges.append((a - 1, b - 1))

parents = list(range(n))
rank = [0] * n

def is_one_alone():
    e0 = find(0)
    return any(find(k) != e0 for k in range(n))
    
def find(e):

    if not (0 <= e < n):
        return None

    comp = [e]
    curr = e
    while parents[comp[-1]] != comp[-1]:
        comp.append(parents[curr])
        curr = parents[curr]

    u = comp.pop()
    while comp:
        parents[comp.pop()] = u 
    
    return parents[e]

def union(e1, e2):

    r1, r2 = find(e1), find(e2)
    if r1 == r2:
        return
    
    if rank[r1] < rank[r2]:
        r1, r2 = r2, r1
    
    counts[r1] += counts[r2]
    parents[r2] = r1

    if rank[r1] == rank[r2]:
        rank[r1] += 1

    return counts[r1]

def is_same_set(e1, e2):
    return find(e1) == find(e2)

num = n
max_so_far = 1
for a, b in edges:
    if not is_same_set(a, b):
        num -= 1
        max_so_far = max(max_so_far, union(a, b))
    
    print(num, max_so_far)
    
