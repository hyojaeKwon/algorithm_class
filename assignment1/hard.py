
nums = [3,1,5,8]

def matrixSolve(nums):
    newNums = []
    newNums.append(1)
    for i in nums:
        newNums.append(i)
    newNums.append(1)
    length = len(newNums)
    matrix = [[0] * length for _ in range(length)]


    for i in range(1,length):
        for j in range(1,length - i):
            k = i + j
            matrix[j][k] = 0
            for q in range(j,k):
                cost = matrix[j][q] + matrix[q + 1][k] + newNums[j-1] * newNums[q] * newNums[k]
                matrix[j][k] = max(cost, matrix[j][k])

    print(matrix[1][length - 1])



matrixSolve(nums)