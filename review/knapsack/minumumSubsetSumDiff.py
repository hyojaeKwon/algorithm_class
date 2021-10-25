#minumum subset of list difference

import sys
Input = sys.stdin.readline

inList = list(map(int,Input().split()))

dp = [[0]*(sum(inList)//2+1) for _ in range(len(inList)+1)]

for i in range(1,)

