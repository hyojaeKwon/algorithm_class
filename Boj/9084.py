import sys
Input = sys.stdin.readline

t = int(Input())
for _ in range(t):
    n = int(Input())
    coin = list(map(int,Input().split()))
    m = int(Input())

    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(m):
        dp[0][i] = 1

    print(dp)

    for i in range(1,n):
        print(i)
        for j in range(1,m):
            if coin[i-1] > m:
                dp[i][j] = dp[i-1][j]
            else:
                plus = 0
                for k in range((dp[i][j]+1)//coin[i]):
                    print(k)
                    plus += dp[i-1][j-(k*coin[i-1])]

            dp[i][j] += plus
            print(dp)



    print(dp[n-1][m-1])


