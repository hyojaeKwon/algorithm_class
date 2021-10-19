line1 = input()
line2 = input()
line3 = input()

dp=[[[0]*(len(line2)+1) for _ in range(len(line1)+1)] for _ in range(len(line3)+1)]

for k in range(1,len(line3)+1):
    for i in range(1,len(line1)+1):
        for j in range(1,len(line2)+1):
            if line1[i-1] == line2[j-1] == line3 [k-1]:
                dp[k][i][j] = dp[k-1][i-1][j-1] + 1
            else:
                dp[k][i][j] = max(dp[k - 1][i][j], dp[k][i - 1][j], dp[k][i][j - 1], dp[k - 1][i - 1][j],dp[k][i - 1][j - 1], dp[k - 1][i][j - 1])

print(dp[-1][-1][-1])
