import sys
Input = sys.stdin.readline

t = int(Input())
for _ in range(t):
    n = int(Input())
    coin = list(map(int,Input().split()))
    m = int(Input())


    #여기서 m+1배열을 만드는 이유는, dp[0]을 1로 둠으로써 1번째 row를 계산하기 위함임.
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for i in range(n):
        for j in range(coin[i],m+1):
            dp[j] = dp[j-coin[i]] + dp[j]

    print(dp)
    print(dp[m])
