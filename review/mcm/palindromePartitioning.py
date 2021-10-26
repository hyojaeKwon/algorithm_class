import sys
Input = sys.stdin.readline

inList = Input().split()
dp = [[False]*(len(inList)+1) for _ in range(len(inList)+1)]

for i in range(len(inList)):
    dp[i+1][i+1] = True
    dp[i+1][i] = True

for i in range(1,len(inList)):
    for j in range(1,len(inList)-i+1):
        if inList[j-1] == inList[j+i-1]:
            if dp[j+1][j+i-1]:
                dp[j][j+i] = True


print(dp)



