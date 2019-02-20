from math import sqrt, fabs

# На плоскости заданы координаты 3 точек
x1, y1 = map(float, input('Input x and y for point A: ').split())
x2, y2 = map(float, input('Input x and y for point B: ').split())
x3, y3 = map(float, input('Input x and y for point C: ').split())
print('\n')

# Проверка ввода
if (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3) == 0:
    print('Uncorrect coordinates')
    raise SystemExit
else:
    print('Correct coordinates')
print('\n')

# Длины сторон треугольника, построенного на этих точках
ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('Length of AB: {:.5g}'.format(ab))
bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
print('Length of BC: {:.5g}'.format(bc))
ca = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
print('Length of CA: {:.5g}'.format(ca))
print('\n')

# Длина высоты, проведенной из наименьшего угла
if ab <= bc and ab <= ca:
    side = ab
elif bc <= ab and bc <= ca:
    side = bc
else:
    side = ca
p = (ab + bc + ca) / 2
height = 2 * sqrt(p * (p - ab) * (p - bc) * (p - ca)) / side
print('Length of height from the smallest angle: {:.5g}'.format(height))
print('\n')

# Ввод координат 4 точки
x4, y4 = map(float, input('Input x and y for point D: ').split())
print('\n')

# Находиться ли точка 4 внутри треугольника
a = (x1 - x4) * (y2 - y1) - (x2 - x1) * (y1 - y4)
b = (x2 - x4) * (y3 - y2) - (x3 - x2) * (y2 - y4)
c = (x3 - x4) * (y1 - y3) - (x1 - x3) * (y3 - y4)
if (a >= 0 and b >= 0 and c >=0) or (a <= 0 and b <= 0 and c <= 0):
    print('Point D is inside triangle')

    # Расстояние от точки 4 до наибольшей стороны
    if ab >= bc and ab >= ca:
        distance = fabs(((x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)) / sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    elif bc >= ab and bc >= ca:
        distance = fabs(((x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2)) / sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2))
    else:
        distance = fabs(((x1 - x3) * (y4 - y3) - (y1 - y3) * (x4 - x3)) / sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2))
    print('Distance from point D to the biggest side: {:.5g}'.format(distance))
else:
    print('Point D is not inside triangle')
print('\n')

# Является ли треугольник равнобедренным
if ab == bc or ab == ca or bc == ca:
    print('Triangle ABC is isosceles')
else:
    print('Triangle ABC is not isosceles')
