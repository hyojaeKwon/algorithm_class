import sys
Input = sys.stdin.readline

n,m = map(int,Input().split())
cost = list(map(int,Input().split()))
pay = list(map(int,Input().split()))
SPAY = sum(pay)
result = SPAY

K = [[0 for _ in range(SPAY+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(SPAY+1):
        if not i or not j:
            K[i][j] = 0
        elif pay[i-1] <= j:
            K[i][j] = max(cost[i-1]+K[i-1][j-pay[i-1]],K[i-1][j])
        else:
            K[i][j] = K[i-1][j]

        if K[i][j] >= m:
            result = min(result,j)

print(result)