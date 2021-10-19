import sys
Input = sys.stdin.readline


x = Input().rstrip()
y = Input().rstrip()

def find(x,y):
    xlen = len(x)
    ylen = len(y)

    dp =[[0]*(xlen+1) for _ in range(ylen+1)]
    for i in range(1,ylen+1):
        for j in range(1,xlen+1):
            if y[i-1] == x[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    number = dp[ylen][xlen]
    result = ''
    i = ylen
    j = xlen
    while number != 0:
        if dp[i][j-1] == (number -1) and dp[i-1][j] == (number - 1):
            result =  x[j-1]+result
            i-=1
            j-=1
            number-=1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
    print(dp[ylen][xlen])
    print(result)

find(x,y)

