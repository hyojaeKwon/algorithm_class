import sys
Input = sys.stdin.readline

def dpFind(n,s,m,inp):
    # 3 5 10
    dp = [[False] * (m+1) for _ in range(n+1)]
    dp[0][s] = True


    for i in range(1,n+1):
        for j in range(m+1):
            if dp[i-1][j]:
                if j + inp[i-1] <= m:
                    dp[i][j + inp[i-1]] = True
                if j - inp[i-1] >= 0:
                    dp[i][j - inp[i-1]] = True

    maxi = -1
    for i in range(len(dp[0])):
        if dp[n][i]:
            maxi = i

    print(maxi)


if __name__ == "__main__":
    n,s,m = map(int,Input().split())
    inp = list(map(int,Input().split()))
    dpFind(n,s,m,inp)