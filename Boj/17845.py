import sys
Input = sys.stdin.readline
n, k = map(int,Input().split())
classList = []

for _ in range(k):
    classList.append(list(map(int,Input().split())))

def find(classList,n,k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(k+1):
        for j in range(n+1):
            if not i or not j:
                dp[i][j] = 0
            elif classList[i-1][1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(  classList[i-1][0]+  dp[i-1][j-classList[i-1][1]]    ,dp[i-1][j]  )
    print(dp[k][n])

find(classList,n,k)