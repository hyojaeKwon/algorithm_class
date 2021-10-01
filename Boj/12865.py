import sys
Input = sys.stdin.readline

n, k = map(int,Input().split())

items = [list(map(int,Input().split())) for i in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    for j in range(k):
        if items[i][0] > j+1:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j-items[i][0]+1] + items[i][1])
print(dp[n][k])


