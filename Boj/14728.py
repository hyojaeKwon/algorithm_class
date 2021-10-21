import sys
Input = sys.stdin.readline

n,t = map(int,Input().rsplit())
time = []
time.append([0]*2)
for i in range(n):
    time.append(list(map(int,Input().split())))
dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        if time[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - time[i][0]] + time[i][1])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][t])
