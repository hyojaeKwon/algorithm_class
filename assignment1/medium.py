import sys
Input = sys.stdin.readline

mat = [[1,3,4],[2,4,6],[6,2,6]]

def rotateMat(mat):
    result = []
    matLen = len(mat)
    for i in range(matLen):
        temp = []
        for j in range(matLen):
            temp.append(mat[matLen-1-i][matLen-1-j])
        result.append(temp)
    return result

