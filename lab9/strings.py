strings = [ 
    '       Маленькая  закоптелая  2+3 + 5   дверь в конце лестницы,  на самом ',
    '    верху, была   отворена. Огарок   освещал беднейшую комнату',
    ' шагов в 10-8   длинойдлиной. ВсюВсю   ее было видно 11 - 7 из сенейсеней. Всё 4+   ',
    '3',
    '       было     разбросано и   в беспорядке, в особенности   разное',
    ' детское тряпье. Через 2 + 4  задний угол была протянута      дырявая простыня.',
]

# Вывод строк
def printStrings(strings, lengthStrings):
    print('')
    for i in range(lengthStrings):
        print(strings[i])
    print('')

# Удаление пробелов
def formatStrings(strings, lengthStrings):
    string = ''
    space = False
    for i in range(lengthStrings):
        for j in range(len(strings[i])):
            if strings[i][j] == ' ' and not string:
                continue
            elif strings[i][j] == ' ' and string and not space:
                string += strings[i][j]
                space = True
            elif strings[i][j] != ' ':
                string += strings[i][j]
                space = False
        strings[i] = ''
        for j in range(len(string)):
            if j == len(string) - 1 and string[j] == ' ':
                continue
            strings[i] += string[j]
        string = ''

# Нахождение длины максимальной строки
def getMaxLengthStrings(strings, lengthStrings):
    maxLengthStrings = 0
    for i in range(lengthStrings):
        if len(strings[i]) > maxLengthStrings:
            maxLengthStrings = len(strings[i])
    return maxLengthStrings

# Отделение символов и чисел
def splitSymbols(strings, lengthStrings):
    for i in range(lengthStrings):
        strings[i] = strings[i].replace('+', ' + ')
        strings[i] = strings[i].replace('-', ' - ')
        strings[i] = strings[i].replace('–', ' – ')
        strings[i] = strings[i].replace('.', ' . ')
        strings[i] = strings[i].replace(',', ' , ')
    for i in range(lengthStrings):
        splitString = strings[i].split()
        for j in range(len(splitString)):
            if splitString[j].isdigit():
                strings[i] = (' ' + splitString[j] + ' ').join(strings[i].split(splitString[j]))

# Выравнивание по ширине
def alignWidth(strings, lengthStrings):
    formatStrings(strings, lengthStrings)
    maxLengthStrings = getMaxLengthStrings(strings, lengthStrings)
    for i in range(lengthStrings):
        for j in range(len(strings[i])):
            if strings[i][j] == ' ':
                break
            if j == len(strings[i]) - 1:
                difLength = maxLengthStrings - len(strings[i])
                if difLength % 2 == 0:
                    strings[i] = (' ' * int((difLength / 2))) + strings[i] + \
                    (' ' * int((difLength / 2)))
                else:
                    strings[i] = (' ' * int((((difLength - 1) / 2) + 1))) + \
                    strings[i] + (' ' * int(((difLength - 1) / 2)))
        j = 0
        amountSpaces = 1
        while len(strings[i]) != maxLengthStrings:
                if strings[i][j] == ' ':
                    strings[i] = strings[i][:j] + ' ' + strings[i][j:]
                    j += amountSpaces
                j += 1
                if j == len(strings[i]):
                    j = 0
                    amountSpaces += 1
    global mode
    mode = 1

# Выравнивание по левому краю
def alignLeft(strings, lengthStrings):
    formatStrings(strings, lengthStrings)
    maxLengthStrings = getMaxLengthStrings(strings, lengthStrings)
    for i in range(lengthStrings):
        if len(strings[i]) < maxLengthStrings:
            strings[i] = strings[i] + (' ' * (maxLengthStrings - len(strings[i])))
    global mode
    mode = 2

# Выравнивание по правому краю
def alignRight(strings, lengthStrings):
    formatStrings(strings, lengthStrings)
    maxLengthStrings = getMaxLengthStrings(strings, lengthStrings)
    for i in range(lengthStrings):
        if len(strings[i]) < maxLengthStrings:
            strings[i] = (' ' * (maxLengthStrings - len(strings[i]))) + strings[i]
    global mode
    mode = 3

# Замена слова
def replaceWord(strings, lengthStrings):
    splitSymbols(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' . ', '. ')
        strings[i] = strings[i].replace(' , ', ', ')
    formatStrings(strings, lengthStrings)
    while True:
        wordOld = input('Введите слово, которое хотите заменить: ')
        if wordOld == '':
            print('Неправильный ввод')
            continue
        wordNew = input('Введите слово, которым хотите замменить: ')
        if wordNew == '':
            print('Неправильный ввод')
            continue
        for i in range(lengthStrings):
            words = strings[i].split()
            for j in range(len(words)):
                if wordOld.lower() == words[j].lower():
                    strings[i] = wordNew.join(strings[i].split(words[j]))
                if wordOld.lower() + '.' == words[j].lower():
                    strings[i] = (wordNew + '.').join(strings[i].split(words[j]))
                if wordOld.lower() + '!' == words[j].lower():
                    strings[i] = (wordNew + '!').join(strings[i].split(words[j]))
                if wordOld.lower() + '?' == words[j].lower():
                    strings[i] = (wordNew + '?').join(strings[i].split(words[j]))
                if wordOld.lower() + ',' == words[j].lower():
                    strings[i] = (wordNew + ',').join(strings[i].split(words[j]))
        splitSymbols(strings, lengthStrings)
        for i in range(lengthStrings):
            strings[i] = strings[i].replace(' . ', '. ')
            strings[i] = strings[i].replace(' , ', ', ')
        formatStrings(strings, lengthStrings)
        break

# Удаление слова
def deleteWord(strings, lengthStrings):
    splitSymbols(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' . ', '. ')
        strings[i] = strings[i].replace(' , ', ', ')
    formatStrings(strings, lengthStrings)
    while True:
        word = input('Введите слово, которое хотите удалить: ')
        if word == '':
            print('Неправильный ввод')
            continue
        for i in range(lengthStrings):
            words = strings[i].split()
            for j in range(len(words)):
                if word.lower() == words[j].lower():
                    strings[i] = ''.join(strings[i].split(words[j]))
                if word.lower() + '.' == words[j].lower():
                    strings[i] = '.'.join(strings[i].split(' ' + words[j]))
                if word.lower() + '!' == words[j].lower():
                    strings[i] = '!'.join(strings[i].split(' ' + words[j]))
                if word.lower() + '?' == words[j].lower():
                    strings[i] = '?'.join(strings[i].split(' ' + words[j]))
                if word.lower() + ',' == words[j].lower():
                    strings[i] = ','.join(strings[i].split(' ' + words[j]))
        splitSymbols(strings, lengthStrings)
        for i in range(lengthStrings):
            strings[i] = strings[i].replace(' . ', '. ')
            strings[i] = strings[i].replace(' , ', ', ')
        formatStrings(strings, lengthStrings)
        j = 0
        for i in range(lengthStrings):
            if i == lengthStrings - j:
                break
            if strings[i] == '':
                del strings[i]
                j += 1
        lengthStrings = lengthStrings - j
        for i in range(lengthStrings):
            splitString = strings[i].split()
            for j in range(len(splitString)):
                if j != len(splitString) - 1 and splitString[j] == '+' and\
             (not splitString[j - 1].isdigit() and splitString[j - 1] != ' '):
                    splitString[j] = ' '
                if j != len(splitString) - 1 and splitString[j] == '+' and\
             (not splitString[j + 1].isdigit() and splitString[j + 1] != ' '):
                    splitString[j] = ' '
                if j != len(splitString) - 1 and splitString[j] == '-' and\
             (not splitString[j - 1].isdigit() and splitString[j - 1] == ' '):
                    splitString[j] = ' '
                if j != len(splitString) - 1 and splitString[j] == '-' and\
             (not splitString[j + 1].isdigit() and splitString[j + 1] == ' '):
                    splitString[j] = ' '
                if j == len(splitString) - 1 and (splitString[j] == '+' or splitString[j] == '+'):
                    splitString[j] = ' '
            strings[i] = '' 
            for j in range(len(splitString)):
                strings[i] += splitString[j] + ' '
        for i in range(lengthStrings):
            strings[i] = strings[i].replace(' . ', '. ')
            strings[i] = strings[i].replace(' , ', ', ')
        formatStrings(strings, lengthStrings)
        j = 0
        for i in range(lengthStrings):
            if i == lengthStrings - j:
                break
            if strings[i] == '':
                del strings[i]
                j += 1
        break

# Замена арифмитических выражений
def replaceArifmetic(strings, lengthStrings):
    splitSymbols(strings, lengthStrings)
    sign = ''
    number1 = ''
    number2 = ''
    flag1 = False
    flag2 = False
    for i in range(lengthStrings):
        splitString = strings[i].split()
        for j in range(len(splitString)):
            if j != len(splitString) - 1 and splitString[j] == '+' and\
             splitString[j - 1].isdigit() and splitString[j + 1].isdigit():
                splitString[j + 1] = str(int(splitString[j - 1]) + int(splitString[j + 1]))
                splitString[j - 1] = ' '
                splitString[j] = ' '
            if j != len(splitString) - 1 and splitString[j] == '-' and \
            splitString[j - 1].isdigit() and splitString[j + 1].isdigit():
                splitString[j] = str(int(splitString[j - 1]) - int(splitString[j + 1]))
                splitString[j - 1] = ' '
                splitString[j + 1] = ' '
            if flag1:
                if splitString[0] == '+' and splitString[1].isdigit():
                    splitString[1] = str(int(number1) + int(splitString[1]))
                    splitString[0] = ' '
                    number1 = ''
                elif splitString[j] == '-' and splitString[j + 1].isdigit():
                    splitString[j + 1] = str(int(number1) - int(splitString[j + 1]))
                    splitString[j] = ' '
                    number1 = ''
                else:
                    strings[i - 1] += str(number1)
                    number1 = ''
            if flag2:
                if splitString[0].isdigit() and sign == '+':
                    strings[i - 1] += ' ' + str(int(number2) + int(splitString[0]))
                    splitString[0] = ' '
                    number2 = ''
                    sign = ''
                if splitString[0].isdigit() and sign == '-':
                    strings[i - 1] += ' ' + str(int(number2) - int(splitString[0]))
                    splitString[0] = ' '
                    number2 = ''
                    sign = ''
                else:
                    strings[i - 1] += ' ' + str(number2) + ' ' + str(sign)
                    number2 = ''
                    sign = ''
            if j == (len(splitString) - 1) and splitString[j].isdigit() and i != 0:
                number1 = splitString[j]
                splitString[j] = ' '
                flag1 = True
            if j == (len(splitString) - 1) and splitString[j - 1].isdigit() and \
            (splitString[j] == '+' or splitString[j] == '-') and i != 0:
                sign = splitString[j]
                number2 = splitString[j - 1]
                splitString[j] = ' '
                splitString[j - 1] = ' '
                flag2 = True
        strings[i] = ''
        for j in range(len(splitString)):
            strings[i] += splitString[j] + ' '
    splitSymbols(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' . ', '. ')
        strings[i] = strings[i].replace(' , ', ', ')
    formatStrings(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' .', '. ')
        strings[i] = strings[i].replace(' ,', ', ')
    formatStrings(strings, lengthStrings)
    j = 0
    for i in range(lengthStrings):
        if i == lengthStrings - j:
            break
        if strings[i] == '':
            del strings[i]
            j += 1

# Предложение с максимальным числом слов
def findSentence(strings, lengthStrings):
    splitSymbols(strings, lengthStrings)
    sentences = []
    indexSentence = 0
    symbols = { 'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0,
                'з': 0,'и': 0,'й': 0,'к': 0,'л': 0,'м': 0,'н': 0,'о': 0,'п': 0,'р': 0,
                'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0,
                'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0 }
    sentences.append(0)
    for i in range(lengthStrings):
        splitString = strings[i].split()
        for j in range(len(splitString)):
            if splitString[j] == '.' or splitString[j] == '!' or splitString[j] == '?':
                indexSentence += 1
                sentences.append(0)
            if not splitString[j].isalpha():
                continue
            for k in range(len(splitString[j])):
                symbols[splitString[j][k].lower()] += 1
            if len(list(filter(lambda s: s == 1, symbols.values()))) == 0:
                    sentences[indexSentence] += 1
            symbols = { 'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0,
                'з': 0,'и': 0,'й': 0,'к': 0,'л': 0,'м': 0,'н': 0,'о': 0,'п': 0,'р': 0,
                'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0,
                'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0 }
    maxWordsSentence = [0, 0]
    for i in range(len(sentences)):
        if sentences[i] > maxWordsSentence[0]:
            maxWordsSentence[0] = sentences[i]
            maxWordsSentence[1] = i + 1
    if maxWordsSentence[0] == 0:
        print('Нет такого предложения')
    else:
        print('Предложение с максимальным числом слов - {0}'.format(maxWordsSentence[1]))
    splitSymbols(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' . ', '. ')
        strings[i] = strings[i].replace(' , ', ', ')
    formatStrings(strings, lengthStrings)
    for i in range(lengthStrings):
        strings[i] = strings[i].replace(' . ', '. ')
        strings[i] = strings[i].replace(' , ', ', ')
        strings[i] = strings[i].replace(' .', '. ')
        strings[i] = strings[i].replace(' ,', ', ')

# Меню
menu = {
    '1': alignWidth,
    '2': alignLeft,
    '3': alignRight,
    '4': replaceWord,
    '5': deleteWord,
    '6': replaceArifmetic,
    '7': findSentence,
}

mode = 0

# Ввод
while True:
    print(
        '\nМеню: '
        '\n1) Выравнивание по ширине.'
        '\n2) Выравние по левому краю.'
        '\n3) Выравнивание по правому краю.'
        '\n4) Замена слова в тексте на другое.'
        '\n5) Удаление слова из текста.'
        '\n6) Замена арифмитических выражений на их результат.'
        '\n7) Предложение с максимальным числом слов, '
        '\n   в которых каждая буква входит не менее двух раз.'
        '\n0) Выход.'
    )
    lengthStrings = len(strings)
    if mode == 1:
        menu['1'](strings, lengthStrings)
    if mode == 2:
        menu['2'](strings, lengthStrings)
    if mode == 3:
        menu['3'](strings, lengthStrings)
    printStrings(strings, lengthStrings)
    commandIndex = input('Введите номер команды: ')
    if '1' <= commandIndex <= '7':
        menu[commandIndex](strings, lengthStrings)
    elif commandIndex == '0':
        break
    else:
        print('Неправильный ввод')
