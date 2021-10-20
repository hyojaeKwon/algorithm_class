import sys
Input = sys.stdin.readline

n,m = map(int,Input().split())

money = []
for i in range(n):
    money.append(list(map(int,Input().split())))

dp = [[0]*(sum(money[n-1])+1) for _ in range(n+1)]
print(money)
print(dp[0])
for i in range(1,n+1):
    for j in range(1,len(dp[0])):
        for k in range(1,m+1):
            if i > j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-money[i][0]]+money[i][k])


print(dp[-1][-1])