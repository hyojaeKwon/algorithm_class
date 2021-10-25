#minumum subset of list difference

import sys
Input = sys.stdin.readline

inList = list(map(int,Input().split()))

dp = [[0]*(sum(inList)//2+1) for _ in range(len(inList)+1)]

dp[0][0] = 1

for i in range(1,len(inList)+1):
    for j in range(sum(inList)//2+1):
        if inList[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j] or dp[i-1][j-inList[i-1]]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

for i in range(1,sum(inList)//2+1,-1):
    if dp[-1][i]:
        print(2*(sum(inList)//2 - i))
