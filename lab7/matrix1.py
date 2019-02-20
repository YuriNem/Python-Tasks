# Цикл ввода
isCorrect = True

while isCorrect:

    # Ввод размера матрицы
    string = input('Input matrix size (max size - 6): ')

    # Проверка строки
    if len(string) != 1 or not (55 > ord(string[0]) > 49):
        isCorrect = False

    # Начало новой итерации при неправильном вводе
    if not isCorrect:
        print('Uncorrect input')
        isCorrect = True
        continue

    # Создание матрицы
    matrixSize = int(string)
    matrix = []
    number = 2

    for i in range(matrixSize):

        # Новая строка
        matrix.append([])

        for j in range(matrixSize):

            # Главная диагональ
            if j == i:
                matrix[i].append(0)

            # Выше главной диагонали
            elif j > i:
                matrix[i].append(1)

            # Ниже главной диагонали
            else:
                matrix[i].append(number)
                number += 1

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

    # Поиск среднего арифметического
    midArifColumn = 0

    for j in range(matrixSize):

        # Сумма столбца
        sumColumn = 0

        for i in range(matrixSize):

            # Подсчет суммы столбца
            sumColumn += matrix[i][j]

        # Среднее арифметическое столбца
        newMidArifColumn = sumColumn / matrixSize

        # Выбор большего среднего арифметического
        midArifColumn = newMidArifColumn if newMidArifColumn > midArifColumn \
        else midArifColumn
    
    # Вывод среднего арифметического
    print('The biggest middle arifmetic of columns: {:.5g}\n'.format(midArifColumn))

    # Выход из цикла ввода
    break
