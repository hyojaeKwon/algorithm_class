import sys
Input = sys.stdin.readline

sys.setrecursionlimit(1001)

list1 = Input().rstrip()
list2 = Input().rstrip()


def lcsFind(list1,list2):
    lenList2 = len(list2)
    lenList1 = len(list1)

    dp = [[0]*(lenList1+1) for _ in range(lenList2+1)]
    if not list2:
        print(0)
        return
    for i in range(1,lenList2+1):
        for j in range(1,lenList1+1):
            if list2[i-1] == list1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    print(dp[lenList2][lenList1])
    print(dp)
    return


lcsFind(list1,list2)
