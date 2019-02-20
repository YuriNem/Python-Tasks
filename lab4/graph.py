print('Input start, end and step.')
x0 = float(input('Start: '))
xn = float(input('End: '))
h = float(input('Step: '))

print('\n           Table x y           ')
print('*--------------*--------------*')
print('|       x      |      y       |')
print('*--------------*--------------*')

x = x0
y = yMax = yMin = (x0 ** 2) - 25

while round(x, 10) <= xn:
    print('|{0:14.8g}|{1:14.8g}|'.format(round(x, 10), y))
    print('|--------------|--------------|')

    if y > yMax:
        yMax = y
    elif y < yMin:
        yMin = y

    x += h
    y = (x ** 2) - 25

print('\nyMin = {0:.8g}, yMax = {1:.8g}'.format(yMin, yMax))

x = x0
y = (x0 ** 2) - 25

while round(x, 10) <= xn:
    d = round((y - yMin) / (yMax - yMin) * 70)

    i = 0
    line = ''
    if round(x, 10) != 0:
        while i <= 70:
            if i == d:
                line += '*'
            elif i == round((-yMin) / (yMax - yMin) * 70):
                line += '|'
            else:
                line += ' '
            i += 1
        print('{0:>8g} |{1}'.format(round(x, 10), line))
    else:
        while i <= 70:
            if i == d:
                line += '*'
            elif i == round((-yMin) / (yMax - yMin) * 70):
                line += '|'
            else:
                line += '-'
            i += 1
        print('{0:>8g} |{1}'.format(0, line))

    x += h
    y = (x ** 2) - 25
