import sys
Input = sys.stdin.readline

str = Input().split()
operator = []
number = []

for i in str:
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        number.append(int(i))
    else:
        operator.append(i)

dp = [[0]*(len(number)+1) for _ in range(len(number)+1)]

for i in range(len(number)):
    dp[i+1][i+1] = number[i]
for i in range(2,len(number)+1):
    for j in range(1, len(number)-i+2 ):
        k = i + j - 1
        dp[j][k] = 0
        for q in range(j,k):
            opera = operator[q-1]
            cost = 0
            if opera == '+':
                cost = dp[j][q] + dp[q+1][k]
            elif opera == '-':
                cost = dp[j][q] - dp[q+1][k]
            elif opera == '*':
                cost = dp[j][q] * dp[q+1][k]
            elif opera == '/':
                cost = dp[j][q] / dp[q+1][k]

            dp[j][k] = max(dp[j][k],cost)
print(dp[1][len(number)])

