import sys
Input = sys.stdin.readline

n, m = map(int,Input().split())
items = [[0,0,0]]
for i in range(n):
    items.append(list(map(int,Input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if items[i][0] > j:
            dp[i][j] = dp[i-1][j]

        else:
            for k in range(1,items[i][2]+1,2):
                if j >= items[i][0]*k:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-items[i][0]*k]+items[i][1]*k,dp[i-1][j])


print(dp[-1][-1])