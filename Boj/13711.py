import sys
Input = sys.stdin.readline
n = int(Input())

x = list(map(int,Input().split()))
y = list(map(int,Input().split()))

xlen = len(x)
ylen = len(y)

dp =[[0]*(xlen+1) for _ in range(ylen+1)]
for i in range(1,ylen+1):
    for j in range(1,xlen+1):
        if y[i-1] == x[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[ylen][xlen])
