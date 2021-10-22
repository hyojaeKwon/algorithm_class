import sys
Input = sys.stdin.readline
for o in range(3):
    n = int(Input())
    Tsum = 0
    table = [[0,0]]
    for i in range(n):
        table.append(list(map(int,Input().split())))
        Tsum += table[-1][0] * table[-1][1]


    if Tsum&1:
        print(0)
        continue

    dp =[[0]*((Tsum//2)+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for k in range(1, table[i][1] + 1):
            for j in range(1,(Tsum//2)+1):
                if not (table[i][0]*k > j):

                    if dp[i-1][j-(table[i][0]*k)]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j])



    if dp[-1][-1]:
        print(1)
    else:
        print(0)