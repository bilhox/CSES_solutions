from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

MOD = 10**9 + 7

distinct_values_count = [0] * n

seen = set()
counter = defaultdict(int)

amount = 0
last_amount = 2
current_distinct_value = a[-1]
temp_count = 1

for i in range(n - 1, -1, -1):

    if current_distinct_value != a[i]:
        if a[i] in counter:
            print("here")
            if counter[current_distinct_value] > 1:
                last_amount = (last_amount * (counter[current_distinct_value] + 1))
                temp_count += counter[current_distinct_value]
            last_amount = last_amount // (counter[a[i]] + 1)
            temp_count -= counter[a[i]]
        else:
            last_amount *= 2 
            temp_count += counter[current_distinct_value]
        current_distinct_value = a[i]

    counter[a[i]] += 1
    print(last_amount, temp_count)
    amount = (amount + last_amount - temp_count) % MOD

print(amount)

# The actual solution

# n=int(input())
# a= list(map(int, input().split()))
# a.sort()
# o=[0]*(n+1)
# o[0]=1
# ps=[1]*n + [0]

# j=-1
# for i in range(1,n):
#     if a[i]!=a[i-1]:
#         j=i-1
#     o[i]+=1+ps[j]
#     o[i]%=(10**9+7)
#     ps[i] = ps[i-1] + o[i]
#     ps[i] %= (10**9+7)
# print(ps[n-1])
