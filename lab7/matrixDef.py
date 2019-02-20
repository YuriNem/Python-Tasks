matrixSize = int(input('Input matrix size: '))
matrix = []

for i in range(matrixSize):
    matrix.append(list(map(int, input('Input row of matrix: ').split())))

for i in range(matrixSize):
    if i == matrixSize - 1:
        print('{}\n'.format(matrix[i]))
    else:
        print(matrix[i])

for i in range(matrixSize):
    for j in range(i, matrixSize):
        matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(matrixSize):
    for j in range(int(matrixSize/2)):
        matrix[i][j], matrix[i][matrixSize - 1 - j] = \
        matrix[i][matrixSize - 1 - j], matrix[i][j]

for i in range(matrixSize):
    if i == matrixSize - 1:
        print('{}\n'.format(matrix[i]))
    else:
        print(matrix[i])

maxSumColumn = 0
indexMaxSumColumn = 0

for j in range(matrixSize):
    sumColumn = 0
    for i in range(matrixSize):
        sumColumn += matrix[i][j]

        if sumColumn > maxSumColumn:
            maxSumColumn = sumColumn
            indexMaxSumColumn = j

for i in range(matrixSize):
    for j in range(indexMaxSumColumn, matrixSize - 1):
        matrix[i][j] = matrix[i][j + 1]
    
for i in range(matrixSize):
    if i == matrixSize - 1:
        print('{}\n'.format(matrix[i]))
    else:
        print(matrix[i])
