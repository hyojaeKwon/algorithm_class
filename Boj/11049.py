import sys
Input = sys.stdin.readline
n = int(Input())
matrix = [[0]*n for _ in range(n)]

d = [ list(map(int,Input().split())) for i in range(n)]

for i in range(1,n):
    for j in range(n-i):
        k = i + j
        matrix[j][k] = 2**32
        for q in range(j,k):
            cost = matrix[j][q] + matrix[q+1][k] + d[j][0]*d[q][1]*d[k][1]
            matrix[j][k] = min(cost,matrix[j][k])

print(matrix[0][n-1])