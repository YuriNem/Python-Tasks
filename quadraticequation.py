# Немушкин Юрий ИУ7-14Б
# Вычисление корней квадратного уравнения

from math import sqrt

a, b, c = map(float, input('Input a, b, c: ').split())
print('{0:.5g}x ** 2 + {1:.5g}x + {2:.5g} = 0\n'.format(a, b, c))

if a == 0:
    if b == 0:
        if c == 0:
            print('x - any number')
        else:
            print('No solutions')
    else:
        if c == 0:
            print('x = 0')
        else:
            x = -c / b
            print('x = {:.5g}'.format(x))
else:
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = -b / (2 * a)
        print('x = {:.5g}'.format(x))
    else:
        if D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            print('x1 = {0:.5g}, x2 = {1:.5g}'.format(x1, x2))
        else:
            print('No solutions')
