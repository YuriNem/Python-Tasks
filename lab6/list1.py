isCorrect = True

while isCorrect:

    # Ввод строки
    s = input('Input array in string: ')

    # Проверка строки
    for i in range(len(s)):
        if not (
        (57 >= ord(s[i]) >= 48) or 
        ord(s[i]) == 45 or 
        ord(s[i]) == 46 or 
        ord(s[i]) == 32
        ):
            isCorrect = False
            break
     
    # Начало новой итерации при неправильном вводе
    if not isCorrect:
        print('Uncorrect input')
        isCorrect = True
        continue

    # Создание массива
    l = list(map(float, s.split()))

    isFirstNegative = False
    sumPositive = 0
    indexLastNegative = None

    for i in range(len(l)):

        # Первый отрицательный элемент
        if not isFirstNegative and l[i] < 0:
            isFirstNegative = True
            indexLastNegative = i

        # Положительные элементы
        elif isFirstNegative and l[i] > 0:
            sumPositive += l[i]

        # Отрицательные элементы
        elif isFirstNegative and l[i] < 0:
            indexLastNegative = i

    # Замена последнего отрицательного элемента суммой положительных
    if indexLastNegative:
        l[indexLastNegative] = sumPositive
        print('Index last negative number is {}'.format(indexLastNegative))
    else:
        print('No negative numbers')

    # Вывод массива
    for i in range(len(l)):
        print('{0:2}: {1:4.5g}'.format(i, l[i]))

    break
