import os

# Выбор файла
def selectFile(fileName):
    fileName = ''
    while not fileName:
        fileName = input('Введите имя файла: ')
        if '\\' in fileName or '/' in fileName:
            print('Некорректное имя файла')
            fileName = ''
    if not (fileName in os.listdir()):
        file = open(fileName, 'w')
        file.close()
        print('Файл создан')
    return fileName

# Создание нового набора записей
def createNotes(fileName):
    if not fileName:
        print('Не выбран файл')
        fileName = selectFile(fileName)
        return fileName
    itemString = ''
    while not itemString:
        itemString = input('Введите название и цену товара через двоиточие: ')
        if not (':' in itemString and itemString.split(':')[1].isdigit()):
            print('Некорректный ввод')
            itemString = ''
    file = open(fileName, 'w')
    file.write('Название:Цена\n')
    file.write(itemString + '\n')
    file.close()
    return fileName

# Добавление записи
def addNote(fileName):
    if not fileName:
        print('Не выбран файл')
        fileName = selectFile(fileName)
        return fileName
    file = open(fileName, 'r')
    itemString = file.readline()
    if itemString != 'Название:Цена\n':
        print('Сначала создайте набор записей')
        file.close()
        fileName = createNotes(fileName)
        return fileName
    file.close()
    itemString = ''
    while not itemString:
        itemString = input('Введите название и цену товара через двоиточие: ')
        if not (':' in itemString and itemString.split(':')[1].isdigit()):
            print('Некорректный ввод')
            itemString = ''
    file = open(fileName, 'a')
    file.write(itemString + '\n')
    file.close()
    return fileName

# Вывод записей
def printNotes(fileName):
    if not fileName:
        print('Не выбран файл')
        fileName = selectFile(fileName)
        return fileName
    file = open(fileName, 'r')
    itemString = file.readline()
    if not itemString:
        print('Файл пуст')
        file.close()
        return fileName
    print('\n**********')
    itemString = file.readline()
    while itemString:
        print('\nНазвание: {0}'.format(itemString.split(':')[0]))
        print('Цена: {0}р.'.format(itemString.split(':')[1][:-1]))
        itemString = file.readline()
    print('\n**********')
    file.close()
    return fileName

# Поиск по одному параметру
def findByOneField(fileName):
    if not fileName:
        print('Не выбран файл')
        fileName = selectFile(fileName)
        return fileName
    file = open(fileName, 'r')
    itemString = file.readline()
    if not itemString:
        print('Файл пуст')
        file.close()
        return fileName
    findString = input('Поиск по одному параметру (название или цена): ')
    findList = []
    itemString = file.readline()
    while itemString:
        if itemString.split(':')[0] == findString or \
            itemString.split(':')[1][:-1] == findString:
            findList.append(itemString)
        itemString = file.readline()
    file.close()
    if not len(findList):
        print('Ничего не найдено')
    else:
        print('\n**********')
        for i in range(len(findList)):
            print('\nНазвание: {0}'.format(findList[i].split(':')[0]))
            print('Цена: {0}р.'.format(findList[i].split(':')[1][:-1]))
        print('\n**********')
    return fileName

# Поиск по двум параметрам
def findByTwoFields(fileName):
    if not fileName:
        print('Не выбран файл')
        fileName = selectFile(fileName)
        return fileName
    file = open(fileName, 'r')
    itemString = file.readline()
    if not itemString:
        print('Файл пуст')
        file.close()
        return fileName
    print('Поиск по двум параметрам')
    itemName = input('Название: ')
    itemPrice = ''
    while not itemPrice:
        itemPrice = input('Цена: ')
        if not itemPrice.isdigit():
            print('Некорректный ввод')
            itemPrice = ''
    findList = []
    itemString = file.readline()
    while itemString:
        if itemString.split(':')[0] == itemName and \
            itemString.split(':')[1][:-1] == itemPrice:
            findList.append(itemString)
        itemString = file.readline()
    file.close()
    if not len(findList):
        print('Ничего не найдено')
    else:
        print('\n**********')
        for i in range(len(findList)):
            print('\nНазвание: {0}'.format(findList[i].split(':')[0]))
            print('Цена: {0}р.'.format(findList[i].split(':')[1][:-1]))
        print('\n**********')
    return fileName

# Меню
menu = {
    '1': selectFile,
    '2': createNotes,
    '3': addNote,
    '4': printNotes,
    '5': findByOneField,
    '6': findByTwoFields,
}

# Имя выбранного файла
fileName = ''

# Индекс команды
commandIndex = ''

# Ввод
while commandIndex != '0':
    if not fileName:
        print('\nФайл не выбран')
    else:
        print('\nВыбранный файл - {0}'.format(fileName))
    print(
        '\nМеню: ',
        '\n1 Выбор файла',
        '\n2 Создание нового набора записей',
        '\n3 Добавление записи',
        '\n4 Вывод всех записей',
        '\n5 Поиск по одному полю',
        '\n6 Поиск по двум полям',
        '\n0 Выход',
    )
    commandIndex = input('\nВведите номер команды: ')
    if '1' <= commandIndex <= '6':
        fileName = menu[commandIndex](fileName)
    elif commandIndex != '0':
        print('Неправильный ввод')
