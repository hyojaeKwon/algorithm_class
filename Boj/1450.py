import sys
Input = sys.stdin.readline

n ,c = map(int,Input().split())
weight = list(map(int,Input().split()))

dp = [[0]*( c + 1 ) for _ in range(n+1)]

print(dp)

for i in range(n+1):
    for j in range(c+1):
        if weight[i] >
