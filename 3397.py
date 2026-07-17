from heapq import *
t = int(input())

facts = [1]
for k in range(1, 21):
    facts.append(facts[-1] * k)

def construction_query(n, k):
    generated = []
    heap = list(range(1, n + 1))
    heapify(heap)
    perm_n = 0
    for i in range(n):
        popped = [heappop(heap)]
        perm_n += facts[n - 1 - i]
        while perm_n < k:
            popped.append(heappop(heap))
            perm_n += facts[n - 1 - i]
        else:
            perm_n -= facts[n - 1 - i]
        generated.append(popped.pop())
        for v in popped:
            heappush(heap, v)
    
    return generated

def k_query(n, a):
    
    k = 1
    heap = list(range(1, n + 1))
    heapify(heap)
    for i in range(n):
        popped = [heappop(heap)]
        while popped[-1] != a[i]:
            k += facts[n - 1 - i]
            popped.append(heappop(heap))
        popped.pop()
        for v in popped:
            heappush(heap, v)
    
    return k


for _ in range(t):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        print(*construction_query(inp[1], inp[2]))
    else:
        print(k_query(inp[1], inp[2:]))
    