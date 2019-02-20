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

    sumAbsNegative = 0
    counterNegative = 0
    midArifNegative = 0

    multiplicationPositive = 1
    counterPositive = 0
    midGeomPositive = 0

    for i in range(len(l)):
    
        # Отрицательные элементы
        if l[i] < 0:
            sumAbsNegative += abs(l[i])
            counterNegative += 1

        # Положительные элементы
        elif l[i] > 0:
            multiplicationPositive *= l[i]
            counterPositive += 1

    if counterNegative:

        # Среднее арифметическое модулей отрицательных чисел
        midArifNegative = sumAbsNegative / counterNegative
        print('Middle arifmetic absolute negative numbers: {:.5g}'
        .format(midArifNegative))
    else:
        print('No negative numbers')

    if counterPositive:

        # Среднее геометрическое положительных чисел
        midGeomPositive = multiplicationPositive ** (1 / counterPositive)
        print('Middle geometric positive numbers: {:.5g}'
        .format(midGeomPositive))
    else:
        print('No positive numbers')

    if midArifNegative != midGeomPositive and counterNegative and counterPositive:
    
        # Вывод большего
        print('{} is bigger'.format('midArifNegative'
        if midArifNegative > midGeomPositive
        else 'midGeomPositive'))

    elif midArifNegative == midGeomPositive and counterNegative and counterPositive:

        # Равенство
        print('They are equal')

    break
