from .point import Point


class Line(object):
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    @property
    def mid(self) -> Point:
        x = round((self.begin.x+self.end.x) / 2)
        y = round((self.begin.y+self.end.y) / 2)

        return Point(x, y)

    @staticmethod
    def loadFromDict(lineDict: dict):
        begin = Point.loadFromDict(lineDict['begin'])
        end = Point.loadFromDict(lineDict['end'])

        return Line(begin, end)