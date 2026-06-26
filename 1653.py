from itertools import combinations
n, x = map(int, input().split())
w = list(map(int, input().split()))
# used = 2**n - 1
count = 0
dp = [0] * (2**n + 1)

DEC = 1 << 31
WEIGHT = DEC - 1

# def rec_2(visited, dp):

#     if visited == 2**n - 1:
#         return (1, 0)
    
#     if dp[visited] != None:
#         return dp[visited]
    
#     min_so_far = (1000, 0)

#     for i in range(n):
#         if visited & (1 << i):
#             continue

#         c, weight = rec_2(visited | (1 << i), dp)

#         if weight + w[i] > x:
#             c += 1
#             weight = w[i]
#         else:
#             weight += w[i]

#         min_so_far = min(min_so_far, (c, weight))

#     dp[visited] = min_so_far

#     return min_so_far

# def rec_1():

#     stack = [0]

#     while stack:
#         state = stack.pop()
#         if dp[state] != None:
#             continue

#         if state == 2**n - 1:
#             dp[state] = (1, 0)
#             continue
        
#         computable = True
#         transitions = []

#         min_so_far = (1000, 0)

#         for i in range(n):
#             if state & (1 << i):
#                 continue

#             if dp[state | (1 << i)] == None:
#                 transitions.append(state | (1 << i))
#                 computable = False
#                 continue

#             c, weight = dp[state | (1 << i)]
#             if weight + w[i] > x:
#                 c += 1
#                 weight = w[i]
#             else:
#                 weight += w[i]
            
#             min_so_far = min(min_so_far, (c, weight))
        
#         if not computable:
#             stack.append(state)
#             stack.extend(transitions)
#         else:
#             dp[state] = min_so_far
    
#     return dp[0]

def rec_4():

    for i in range(n):
        dp[((1 << n) - 1) ^ (1 << i)] = DEC + w[i]

    default = (1 << n) - 1
    for k in range(2, n + 1):
        for u in combinations(range(n), k):

            bitmask = default
            for v in u:
                bitmask ^= (1 << v)

            min_so_far = 10**12

            for i in u:

                r = dp[bitmask | (1 << i)]
                weight_part = r & WEIGHT
                if weight_part + w[i] > x:
                    r ^= weight_part
                    r += w[i]
                    r += DEC
                else:
                    r += w[i]
                
                min_so_far = min(min_so_far, r)
            
            dp[bitmask] = min_so_far
    
    return dp[0]
            


print(rec_4() >> 31)
# print((sum(w) + x) // x)