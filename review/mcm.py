        import sys
Input = sys.stdin.readline

matrixList = list(map(int,Input().split()))
matrixList.insert(0,1)
matrixList.append(1)

matrix = [[0]*len(matrixList) for _ in range(len(matrixList))]

for i in range(1,len(matrixList)):
    for j in range(1, len(matrixList)-i):
        k = i + j
        matrix[j][k] = 0
        for q in range(j,k):
            cost = matrix[j][q] + matrix[q+1][k] + matrixList[j-1]*matrixList[q]*matrixList[k]
            matrix[j][k] = max(cost,matrix[j][k])
print(matrix)