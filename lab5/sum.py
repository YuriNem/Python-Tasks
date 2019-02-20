# Вывод элементов ряда и суммы ряда с шагом

eps = float(input('Input precision: ')) # точность
x = float(input('Input x: ')) # x
step = int(input('Input step: ')) # шаг
iter = int(input('Input amount of iteration: ')) # колличество итерация

if iter == 0:
    print('Amount of iteration = 0')
    raise SystemExit

n = 1
curItem = (x**3) / 5
if abs(curItem) <= eps:
    print('Epsilon > 1 item')
    raise SystemExit

sumItems = 0
print('*-----------*-----------*-----------*')
print('|     n     |  curItem  |    sum    |')
print('*-----------*-----------*-----------*')

while abs(curItem) > eps and iter != 0:
    sumItems += curItem
    if (n - 1) % step == 0:
        print('|{0:11.5g}|{1:11.5g}|{2:11.5g}|'.format(n, curItem, sumItems)) # вывод итераций с шагом
        print('*-----------*-----------*-----------*')
    n += 1
    curItem = ((-1)**(n + 1)) * (x**(2*n + 1)) / (4*(n**2) + 1)
    iter -= 1

print('Last iteration: {}'.format(n - 1))
print('Sum = {:.5g}'.format(sumItems))
