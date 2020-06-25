from pkg.graphics.all import Color, Frame, Drawable
from pkg.geometry.all import Rect


class RectView(Drawable):
    def __init__(self, rect=Rect.zero(), color=Color.green()):
        super().__init__()
        self.color = color
        self.rect = rect

    def update(self, rect: Rect):
        self.rect = rect

    def draw(self, frame: Frame):
        if self.rect:
            frame.drawRect(self.rect, 2, self.color)


assert issubclass(RectView, Drawable)