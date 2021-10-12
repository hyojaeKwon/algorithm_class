
def rotateMat(mat):
    result = []
    matLen = len(mat)
    for i in range(matLen):
        temp = []
        for j in range(matLen):
            temp.append(mat[matLen-1-i][matLen-1-j])
        result.append(temp)
    print(result)

