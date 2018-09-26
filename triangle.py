from math import sqrt

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
                if sideFirst.getLength() <= sideSecond.getLength():
                    return sideFirst
                else:
                    return sideThird
            else:
                if sideSecond.getLength() <= sideThird.getLength():
                    return sideSecond
                else:
                    return sideThird
        
        sideFirstLength = self.sideFirst.getLength()
        sideSecondLength = self.sideSecond.getLength()
        sideThirdLength = self.sideThird.getLength()
        semiperimeter = (sideFirstLength + sideSecondLength + sideThirdLength) / 2
        sideTheSmallest = getTheSmallestSide(self.sideFirst, self.sideSecond, self.sideThird)
        return 2 * sqrt(semiperimeter * (semiperimeter - sideFirstLength) * (semiperimeter - sideSecondLength) * (semiperimeter - sideThirdLength)) / sideTheSmallest.getLength()

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
                if sideFirst.getLength() >= sideSecond.getLength():
                    return sideFirst
                else:
                    return sideThird
            else:
                if sideSecond.getLength() >= sideThird.getLength():
                    return sideSecond
                else:
                    return sideThird
        
        if self.isPointInside(point):
            sideTheBigget = getTheBiggestSide(self.sideFirst, self.sideSecond, self.sideThird)
            return sideTheBigget
        else:
            return FALSE

    def isIsosceles(self):
        sideFirstLength = self.sideFirst.getLength()
        sideSecondLength = self.sideSecond.getLength()
        sideThirdLength = self.sideThird.getLength()
        return sideFirstLength == sideSecondLength or sideFirstLength == sideThirdLength or sideSecondLength == sideThirdLength

point1 = Point(1, 1)
point2 = Point(2, 3)
point3 = Point(3, 1)

side12 = Side(point1, point2)
side23 = Side(point2, point3)
side31 = Side(point3, point1)
print(side12.getLength(), side23.getLength(), side31.getLength())

triangle123 = Triangle(side12, side23, side31)
pointTest = Point(2, 2)
print(triangle123.getHeightFromTheSmallestAngle(), triangle123.isPointInside(pointTest), triangle123.getDistanceFromPointToTheBiggestSide(pointTest), triangle123.isIsosceles())
