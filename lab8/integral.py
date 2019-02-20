# Функция
def f(x):
    return x

# Интеграл
def F(a, b):
    return (b**2 / 2) - (a**2 / 2)

# Метод средних прямоугольников
def midpoint(a, b, n):
    result = 0
    h = (b - a) / n
    for i in range(n):
        result += f(a + h * (i + 0.5))
    result *= h
    return result

# Метод парабол
def parabolas(a, b, n):
    if n % 2 != 0:
        return '-'
    h = (b - a) / n
    sum1 = 0
    for i in range(1, n + 1, 2):
        xi = a + i * h
        sum1 += f(xi)
    sum2 = 0
    for i in range(2, n, 2):
        xi = a + i * h
        sum2 += f(xi)
    result = (h / 3) * (f(a) + 4 * sum1 + 2 * sum2 + f(b))
    return result

# Вычисление интеграла с точностью эпсилон и ошибок
def findWithEps(methodName, method, a, b, e):
    n = 2
    while abs(method(a, b, 2 * n) - method(a, b, n)) >= e:
        n *= 2
    itg = F(a, b)
    methodValue = method(a, b, n)
    absoluteError = abs(F(a, b) - method(a, b, n))
    relativeError = abs((F(a, b) - method(a, b, n)) / F(a, b))

    # Вывод интеграла с точностью эпсилон и ошибок
    print('\nIntegral: {0:.10g}'.format(itg))
    print('Amount of splitting: {0}'.format(n))
    print('Integral with eps ({0}): {1:.10g}'.format(methodName, methodValue))
    print('Absolute error: {0:.10g}'.format(absoluteError))
    print('Relative error: {0:.10g}'.format(relativeError))

# Ввод данных
error = False
try:
    a = float(input('Input start value: '))
    b = float(input('Input end value: '))
    if a == b:
        raise ValueError
    n1 = int(input('Input first amount of splitting: '))
    n2 = int(input('Input second amount of splitting: '))
except ValueError:
    error = True

# Ошибка ввода
if error:
    print('Uncorrect input')

else:
    # Нахождение интегралов
    midpointItg1 = midpoint(a, b, n1)
    midpointItg2 = midpoint(a, b, n2)
    parabolasItg1 = parabolas(a, b, n1)
    if parabolasItg1 == '-':
        parabolasItg1 = '---------------'
    else:
        parabolasItg1 = '{0:15.10g}'.format(parabolasItg1)
    parabolasItg2 = parabolas(a, b, n2)
    if parabolasItg2 == '-':
        parabolasItg2 = '---------------'
    else:
        parabolasItg2 = '{0:15.10g}'.format(parabolasItg2)

    # Вывод значений интегралов
    print('\n          -------------------------------------')
    print('Splitting | {0:15} | {1:15} |'.format(n1, n2))
    print('          -------------------------------------')
    print('Midpoint  | {0:15.10g} | {1:15.10g} |'.format(midpointItg1, midpointItg2))
    print('Parabolas | {0} | {1} |'.format(parabolasItg1, parabolasItg2))
    print('          -------------------------------------\n')

    # Ввод точности и оценка погрешности 
    try:
        e = float(input('Input eps: '))
        if abs(F(a, b) - midpoint(a, b, 2 * n2)) >= abs(F(a, b) - parabolas(a, b, 2 * n2)):
            findWithEps('midpoint', midpoint, a, b, e)
        else:
            findWithEps('parabolas', parabolas, a, b, e)
    except ValueError:
        print('Uncorrect input')
