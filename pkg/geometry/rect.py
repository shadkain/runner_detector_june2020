from .point import Point


class Rect(object):
    def __init__(self, topLeft: Point, bottomRight: Point):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def __str__(self):
        return f'top-left: {self.topLeft}, bottom-right: {self.bottomRight}'

    def copy(self):
        return Rect(self.topLeft.copy(), self.bottomRight.copy())

    def moveX(self, xOffset: int):
        self.topLeft.x += xOffset
        self.bottomRight.x += xOffset

    def moveY(self, yOffset: int):
        self.topLeft.y += yOffset
        self.bottomRight.y += yOffset

    @property
    def topRight(self) -> Point:
        return Point(self.bottomRight.x, self.topLeft.y)

    @property
    def bottomLeft(self) -> Point:
        return Point(self.topLeft.x, self.bottomRight.y)

    @property
    def minX(self) -> int:
        return self.topLeft.x

    @property
    def maxX(self) -> int:
        return self.bottomRight.x

    @property
    def minY(self) -> int:
        return self.topLeft.y

    @property
    def maxY(self) -> int:
        return self.bottomRight.y

    @property
    def width(self) -> int:
        return self.maxX - self.minX

    @property
    def height(self) -> int:
        return self.maxY - self.minY

    @staticmethod
    def zero():
        return Rect(Point.zero(), Point.zero())

    @staticmethod
    def loadFromDict(rectDict: dict):
        topLeft = Point.loadFromDict(rectDict['top-left'])
        bottomRight = Point.loadFromDict(rectDict['bottom-right'])
        return Rect(topLeft, bottomRight)