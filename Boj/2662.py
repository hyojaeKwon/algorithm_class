import sys
Input = sys.stdin.readline

n,m = map(int,Input().split())


#Knapsack dp changing
money = [[0 for _ in range(m+1)]]
for i in range(n):
    money.append(list(map(int,Input().split())))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i][j-1],money[i][j])
        for k in range(1,i+1):
                       else:
                sol[j]
            if dp[i][j] < money[i-k][j] + dp[k][j-1]:
                dp[i][j] = money[i-k][j] + dp[k][j-1]

print(dp[-1][-1])