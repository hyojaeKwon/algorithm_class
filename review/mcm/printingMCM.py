import sys
Input = sys.stdin.readline

inList = list(map(int,Input().split()))

dp = [[[0]*len(inList) for _ in range(len(inList))]for _ in range(2)]
print(dp)
def find(i,j,dp):
    if i == j:
        print(i)
        return
    print("(")
    num = dp[1][i][j]

    find(i,num,dp)

    find(i+num,j,dp)

    print(")")

for i in range(2,len(inList)):
    for j in range(1,len(inList)-i+1):
        k = i + j - 1
        MIN = sys.maxsize
        dp[0][j][k] = MIN
        for q in range(j,k):
            cost = dp[0][i][q] + dp[0][q+1][k] + inList[i-1] * inList[q] * inList[k]
            if dp[0][j][k] > cost:
                dp[0][j][k] = cost
                dp[1][j][k] = q

find(1,len(inList)-1,dp)




