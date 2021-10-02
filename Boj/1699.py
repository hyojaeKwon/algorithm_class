import sys
Input = sys.stdin.readline


def find(dp,n):
    for i in range(1,n+1):
        for j in range(1,i):
            if j**2 > i:
                break
            dp[i] = min(dp[i],dp[i-j**2] +1)
    print(dp[n])

if __name__ == "__main__":
    n = int(Input())
    dp = [i for i in range(n + 1)]
    find(dp,n)

