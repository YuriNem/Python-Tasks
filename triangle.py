from math import sqrt, fabs

pointFirstX, pointFirstY = map(int, input('Input x and y for first point: ').split())
pointSecondX, pointSecondY = map(int, input('Input x and y for second point: ').split())
pointThirdX, pointThirdY = map(int, input('Input x and y for third point: ').split())
print('\n')

sideFirstLength = sqrt((pointSecondX - pointFirstX) ** 2 + (pointSecondY - pointFirstY) ** 2)
print('Length of first side: {:.5g}'.format(sideFirstLength))
sideSecondLength = sqrt((pointThirdX - pointSecondX) ** 2 + (pointThirdY - pointSecondY) ** 2)
print('Length of second side: {:.5g}'.format(sideSecondLength))
sideThirdLength = sqrt((pointFirstX - pointThirdX) ** 2 + (pointFirstY - pointThirdY) ** 2)
print('Length of third side: {:.5g}'.format(sideThirdLength))
print('\n')

if sideFirstLength <= sideSecondLength and sideFirstLength <= sideThirdLength:
    sideTheSmallestLength = sideFirstLength
elif sideSecondLength <= sideFirstLength and sideSecondLength <= sideThirdLength:
    sideTheSmallestLength = sideSecondLength
else:
    sideTheSmallestLength = sideThirdLength
semiperimeter = (sideFirstLength + sideSecondLength + sideThirdLength) / 2
heightFromTheSmallestAngle = 2 * sqrt(semiperimeter * (semiperimeter - sideFirstLength) * (semiperimeter - sideSecondLength) * (semiperimeter - sideThirdLength)) / sideTheSmallestLength
print('Length of height from the smallest angle: {:.5g}'.format(heightFromTheSmallestAngle))
print('\n')

pointFourthX, pointFourthY = map(int, input('Input x and y for fourth point: ').split())
print('\n')
a = (pointFirstX - pointFourthX) * (pointSecondY - pointFirstY) - (pointSecondX - pointFirstX) * (pointFirstY - pointFourthY)
b = (pointSecondX - pointFourthX) * (pointThirdY - pointSecondY) - (pointThirdX - pointSecondX) * (pointSecondY - pointFourthY)
c = (pointThirdX - pointFourthX) * (pointFirstY - pointThirdY) - (pointFirstX - pointThirdX) * (pointThirdY - pointFourthY)
if (a >= 0 and b >= 0 and c >=0) or (a <= 0 and b <= 0 and c <= 0):
    print('Point is inside triangle')
    if sideFirstLength >= sideSecondLength and sideFirstLength >= sideThirdLength:
        distanceFromPointToTheBiggestSide = fabs(((pointSecondX - pointFirstX) * (pointFourthY - pointFirstY) - (pointSecondY - pointFirstY) * (pointFourthX - pointFirstX)) / sqrt((pointSecondX - pointFirstX) ** 2 + (pointSecondY - pointFirstY) ** 2))
    elif sideSecondLength >= sideFirstLength and sideSecondLength >= sideThirdLength:
        distanceFromPointToTheBiggestSide = fabs(((pointThirdX - pointSecondX) * (pointFourthY - pointSecondY) - (pointThirdY - pointSecondY) * (pointFourthX - pointSecondX)) / sqrt((pointThirdX - pointSecondX) ** 2 + (pointThirdY - pointSecondY) ** 2))
    else:
        distanceFromPointToTheBiggestSide = fabs(((pointFirstX - pointThirdX) * (pointFourthY - pointThirdY) - (pointFirstY - pointThirdY) * (pointFourthX - pointThirdX)) / sqrt((pointFirstX - pointThirdX) ** 2 + (pointFirstY - pointThirdY) ** 2))
    print('Distance from point to the biggest side: {:.5g}'.format(distanceFromPointToTheBiggestSide))
else:
    print('Point is not inside triangle')
print('\n')

if sideFirstLength == sideSecondLength or sideFirstLength == sideThirdLength or sideSecondLength == sideThirdLength:
    print('Triangle is isosceles')
else:
    print('Triangle is not isosceles')
