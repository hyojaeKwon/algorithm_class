import sys
Input = sys.stdin.readline

n = int(Input())
GList = list(map(int,Input().split()))
find = int(Input())
fList = list(map(int,Input().split()))
sumG = sum(GList)

dp = [[0]*(sumG+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(sumG+1):


        if i == 0 or j == 0:
            dp[i][j] = 0
        elif dp[i-1][j]:
            dp[i][abs(j-GList[i-1])] = 1
            dp[i][j] = 1
            if j + GList[i-1] <= sumG:
                dp[i][j+GList[i-1]] = 1
        elif i > 0 and GList[i-1] == j:
            dp[i][GList[i-1]] =1
        elif dp[i][j]:
            continue
        else:
            dp[i][j] = dp[i-1][j]

answer = []
for i in fList:
    if i > sumG:
        answer.append(False)
    elif dp[n][i]:
        answer.append(True)
    else:
        answer.append(False)

for i in answer:
    if i:
        print("Y",end=' ')
    else:
        print("N",end=' ')
