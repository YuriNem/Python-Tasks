#Немушкин Юрий ИУ7-14Б
#Попытка написать triangle с помощью ООП

from math import sqrt, fabs

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Side():
    def __init__(self, pointFirst, pointSecond):
        self.pointFirst = pointFirst
        self.pointSecond = pointSecond

    def getLength(self):
        return sqrt((self.pointSecond.x - self.pointFirst.x) ** 2 + (self.pointSecond.y - self.pointFirst.y) ** 2)

class Triangle():
    def __init__(self, sideFirst, sideSecond, sideThird):
        self.sideFirst = sideFirst
        self.sideSecond = sideSecond
        self.sideThird = sideThird

    def getHeightFromTheSmallestAngle(self):
        def getTheSmallestSide(sideFirst, sideSecond, sideThird):
            if sideFirst.getLength() <= sideSecond.getLength():
                if sideFirst.getLength() <= sideThird.getLength():
                    return sideFirst
                else:
                    return sideThird
            else:
                if sideSecond.getLength() <= sideThird.getLength():
                    return sideSecond
                else:
                    return sideThird
        
        sideTheSmallest = getTheSmallestSide(self.sideFirst, self.sideSecond, self.sideThird)
        sideTheSmallestLength = sideTheSmallest.getLength()
        sideFirstLength = self.sideFirst.getLength()
        sideSecondLength = self.sideSecond.getLength()
        sideThirdLength = self.sideThird.getLength()
        semiperimeter = (sideFirstLength + sideSecondLength + sideThirdLength) / 2
        return 2 * sqrt(semiperimeter * (semiperimeter - sideFirstLength) * (semiperimeter - sideSecondLength) * (semiperimeter - sideThirdLength)) / sideTheSmallestLength

    def isPointInside(self, point):
        pointFirstX = self.sideFirst.pointFirst.x
        pointFirstY = self.sideFirst.pointFirst.y
        pointSecondX = self.sideSecond.pointFirst.x
        pointSecondY = self.sideSecond.pointFirst.y
        pointThirdX = self.sideThird.pointFirst.x
        pointThirdY = self.sideThird.pointFirst.y
        a = (pointFirstX - point.x) * (pointSecondY - pointFirstY) - (pointSecondX - pointFirstX) * (pointFirstY - point.y)
        b = (pointSecondX - point.x) * (pointThirdY - pointSecondY) - (pointThirdX - pointSecondX) * (pointSecondY - point.y)
        c = (pointThirdX - point.x) * (pointFirstY - pointThirdY) - (pointFirstX - pointThirdX) * (pointThirdY - point.y)
        return (a >= 0 and b >= 0 and c >=0) or (a <= 0 and b <= 0 and c <= 0)

    def getDistanceFromPointToTheBiggestSide(self, point):
        def getTheBiggestSide(sideFirst, sideSecond, sideThird):
            if sideFirst.getLength() >= sideSecond.getLength():
                if sideFirst.getLength() >= sideThird.getLength():
                    return sideFirst
                else:
                    return sideThird
            else:
                if sideSecond.getLength() >= sideThird.getLength():
                    return sideSecond
                else:
                    return sideThird
        
        if self.isPointInside(point):
            sideTheBiggest = getTheBiggestSide(self.sideFirst, self.sideSecond, self.sideThird)
            pointFirstX = sideTheBiggest.pointFirst.x
            pointFirstY = sideTheBiggest.pointFirst.y
            pointSecondX = sideTheBiggest.pointSecond.x
            pointSecondY = sideTheBiggest.pointSecond.y
            return fabs(((pointSecondX - pointFirstX) * (point.y - pointFirstY) - (pointSecondY - pointFirstY) * (point.x - pointFirstX)) / sqrt((pointSecondX - pointFirstX) ** 2 + (pointSecondY - pointFirstY) ** 2))
        else:
            return

    def isIsosceles(self):
        sideFirstLength = self.sideFirst.getLength()
        sideSecondLength = self.sideSecond.getLength()
        sideThirdLength = self.sideThird.getLength()
        return sideFirstLength == sideSecondLength or sideFirstLength == sideThirdLength or sideSecondLength == sideThirdLength

pointFirstX, pointFirstY = map(int, input('Input x and y for first point: ').split())
pointFirst = Point(pointFirstX, pointFirstY)
pointSecondX, pointSecondY = map(int, input('Input x and y for second point: ').split())
pointSecond = Point(pointSecondX, pointSecondY)
pointThirdX, pointThirdY = map(int, input('Input x and y for third point: ').split())
pointThird = Point(pointThirdX, pointThirdY)
print('\n')

sideFirst = Side(pointFirst, pointSecond)
print('Length of first side: {:.5g}'.format(sideFirst.getLength()))
sideSecond = Side(pointSecond, pointThird)
print('Length of second side: {:.5g}'.format(sideSecond.getLength()))
sideThird = Side(pointThird, pointFirst)
print('Length of third side: {:.5g}'.format(sideThird.getLength()))
print('\n')

triangle = Triangle(sideFirst, sideSecond, sideThird)
print('Length of height from the smallest angle: {:.5g}'.format(triangle.getHeightFromTheSmallestAngle()))
print('\n')
pointFourthX, pointFourthY = map(int, input('Input x and y for fourth point: ').split())
pointFourth = Point(pointFourthX, pointFourthY)
print('\n')
if triangle.isPointInside(pointFourth):
    print('Point is inside triangle')
    print('Distance from point to the biggest side: {:.5g}'.format(triangle.getDistanceFromPointToTheBiggestSide(pointFourth)))
else:
    print('Point is not inside triangle')
print('\n')
if triangle.isIsosceles():
    print('Triangle is isosceles')
else:
    print('Triangle is not isosceles')
