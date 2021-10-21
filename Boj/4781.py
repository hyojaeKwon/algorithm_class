import sys
Input = sys.stdin.readline


while True:
    n,m = map(float,Input().split())
    n,m =int(n), int(m*100+0.5)
    if n==0 and m==0:
        break
    lCase = [[0, 0]]
    for i in range(n):
        c, t = map(float, Input().split())
        c, t = int(c), int(t * 100 + 0.5)
        lCase.append([c, t])
    dp = [[0] * int(m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j < lCase[i][1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i][j - lCase[i][1]] + lCase[i][0], dp[i - 1][j],
                               dp[i - 1][j - lCase[i][1]] + lCase[i][0])

    print(dp[-1][-1])

