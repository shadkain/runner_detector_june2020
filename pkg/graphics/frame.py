import cv2
from .color import Color
from pkg.geometry.all import Point, Line, Rect


class Frame(object):
    def __init__(self, data, rect=None):
        self.data = data
        if not rect:
            self.rect = Rect(Point.zero(), Point(self.width, self.height))
        else:
            self.rect = rect

    @property
    def width(self) -> int:
        return self.data.shape[1]

    @property
    def height(self) -> int:
        return self.data.shape[0]

    def fit(self, point: Point) -> Point:
        xy = [point.x, point.y]
        for i, pair in enumerate([(point.x, self.width), (point.y, self.height)]):
            if pair[0] < 0:
                xy[i] = 0
            elif pair[0] > pair[1]:
                xy[i] = pair[1]

        return Point(xy[0], xy[1])

    def crop(self, rect: Rect):
        frameRect = Rect(self.fit(rect.topLeft), self.fit(rect.bottomRight))
        return Frame(self.data[frameRect.minY:frameRect.maxY, frameRect.minX:frameRect.maxX], frameRect)

    def drawCircle(self, center: Point, radius: int, color: Color):
        cv2.circle(self.data, center.pair, radius, color.bgr, thickness=-1, lineType=cv2.FILLED)

    def drawLine(self, line: Line, thickness: int, color: Color):
        cv2.line(self.data, line.begin.pair, line.end.pair, color.bgr, thickness=thickness, lineType=cv2.LINE_AA)

    def drawLineByPoints(self, begin: Point, end: Point, thickness: int, color: Color):
        self.drawLine(Line(begin, end), thickness, color)

    def drawRect(self, rect: Rect, thickness: int, color: Color):
        cv2.rectangle(self.data, rect.topLeft.pair, rect.bottomRight.pair, color.bgr, thickness=thickness, lineType=cv2.LINE_AA)