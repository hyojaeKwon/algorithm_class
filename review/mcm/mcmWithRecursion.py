import sys
Input = sys.stdin.readline

inList = list(map(int,Input().split()))

def mcm(inList,i,j):

    if i == j:
        return 0

    MIN = sys.maxsize

    for k in range(i,j):
        temp = mcm(inList,i,k) + mcm(inList,k+1,j) + inList[i-1]*inList[k]*inList[j]

        if temp < MIN:
            MIN = temp

        return MIN


n = len(inList)
print(mcm(inList,1,n-1))