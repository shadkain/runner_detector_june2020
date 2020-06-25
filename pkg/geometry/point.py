class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    @property
    def pair(self) -> (int, int):
        return (self.x, self.y)

    @staticmethod
    def loadFromDict(pointDict: dict):
        return Point(pointDict['x'], pointDict['y'])

    @staticmethod
    def zero():
        return Point(0, 0)

    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'

    def __json__(self):
        return self.__dict__