from pkg.graphics.all import Color, Frame, Drawable
from pkg.geometry.all import Line, Point


class TrackView(Drawable):
    def __init__(self, startLine: Line, endLine: Line, color: Color):
        super().__init__()
        self.startLine = startLine
        self.endLine = endLine
        self.color = color

    def draw(self, frame):
        frame.drawLine(self.startLine, 2, self.color)
        frame.drawLine(Line(self.startLine.mid, Point(self.startLine.mid.x, 0)), 1, self.color)

        frame.drawLine(Line(self.startLine.begin, self.endLine.begin), 2, self.color)
        frame.drawLine(Line(self.startLine.end, self.endLine.end), 2, self.color)
        frame.drawLine(Line(self.startLine.mid, self.endLine.mid), 1, self.color)

        frame.drawLine(self.endLine, 2, self.color)
        frame.drawLine(Line(self.endLine.mid, Point(self.endLine.mid.x, 0)), 1, self.color)


assert issubclass(TrackView, Drawable)