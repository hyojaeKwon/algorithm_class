import sys
Input = sys.stdin.readline

str = Input().rstrip()

strLen = len(str)
result = 0
dp = [[False]*(strLen+1) for _ in range(strLen+1)]
for i in range(1,strLen+1):
    for j in range(i,strLen+1):
        if i==1 :
            dp[j][j] = True
            result += 1
        elif i==2:
            if str[j-i] == str[j-1]:
                dp[j-i+1][j] = True
                result += 1

        elif str[j-i] == str[j-1]:
            if dp[j-i+2][j-1]==True:
                dp[j - i + 1][j] = True
                result += 1

print(result)