# Цикл ввода
isCorrect = True

while isCorrect:

    # Ввод размера матрицы
    string = input('Input matrix size (max size - 8): ')

    # Проверка строки
    if len(string) != 1 or not (57 > ord(string[0]) > 49):
        isCorrect = False

    # Начало новой итерации при неправильном вводе
    if not isCorrect:
        print('Uncorrect input')
        isCorrect = True
        continue

    # Создание матрицы
    matrixSize = int(string)
    matrix = []
    i = -1

    while (i + 1) != matrixSize:

        # Счетчик ввода
        i += 1

        # Ввод строки
        string = input('Input row of matrix: ')

        # Проверка длины строки
        if not len(list(string.split())) == matrixSize:
            isCorrect = False

        # Начало новой итерации при неправильном вводе
        if not isCorrect:
            print('Uncorrect input')
            isCorrect = True
            i -= 1
            continue

        # Проверка строки
        for j in range(len(string)):
            if not (57 >= ord(string[j]) >= 48 \
            or ord(string[j]) == 45 or ord(string[j]) == 32):
                isCorrect = False
                break
     
        # Начало новой итерации при неправильном вводе
        if not isCorrect:
            print('Uncorrect input')
            isCorrect = True
            i -= 1
            continue

        # Создание строки матрицы
        matrix.append(list(map(int, string.split())))

    # Создание строки для вывода
    printMatrix = ''

    for i in range(matrixSize):
        for j in range(matrixSize):

            # Начало строки
            if j == 0:
                printMatrix += '[ {:2}, '.format(matrix[i][j])

            # Конец строки
            elif j == matrixSize - 1:
                printMatrix += '{:2} ]\n'.format(matrix[i][j])

            # Строка
            else:
                printMatrix += '{:2}, '.format(matrix[i][j])

    # Вывод матрицы
    print(printMatrix)

    # Поворачиваем матрицу
    for i in range(matrixSize):
        for j in range(int(matrixSize/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][matrixSize - 1 - j]
            matrix[i][matrixSize - 1 - j] = temp

    # Создание строки для вывода
    printMatrix = ''

    for i in range(matrixSize):
        for j in range(matrixSize):

            # Начало строки
            if j == 0:
                printMatrix += '[ {:2}, '.format(matrix[i][j])

            # Конец строки
            elif j == matrixSize - 1:
                printMatrix += '{:2} ]\n'.format(matrix[i][j])

            # Строка
            else:
                printMatrix += '{:2}, '.format(matrix[i][j])

    # Вывод матрицы
    print(printMatrix)

    # Выход из цикла ввода
    break
