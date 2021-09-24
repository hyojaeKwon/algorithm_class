import sys
Input = sys.stdin.readline

matrix = [[1,3,4],[2,4,6],[6,2,6]]
matrixLen = len(matrix)


#NxN matrix 인 점을 이용한다.
answer = []
for i in range(matrixLen):
    temp = []
    for j in range(matrixLen):
        temp.append(matrix[matrixLen-1-i][matrixLen-1-j])
    answer.append(temp)

print(answer)