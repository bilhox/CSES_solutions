import sys
n=int(input())
q,v=[],[]
for line in sys.stdin:
 a,b=map(int,line.split())
 q.append(a)
 v.append(b)
q.sort()
v.sort()
t=0
for i in range(n-1):
 t+=(q[i+1]-q[i]+v[i+1]-v[i])*(i+1)*(n-i-1)
print(t)