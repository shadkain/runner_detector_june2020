from pkg.geometry.all import *


class Tracker(object):
    def __init__(self, backSpace: int, frontSpace: int):
        self.backSpace = backSpace
        self.frontSpace = frontSpace

    def track(self, trackerRect: Rect, observableRect: Rect):
        return self.__trackHorizontally(trackerRect, observableRect)

    def __trackHorizontally(self, trackerRect: Rect, observableRect: Rect):
        widthDiff = trackerRect.width - observableRect.width
        positionDiff = observableRect.topLeft.x - trackerRect.topLeft.x

        trackerRect.moveX(positionDiff - int(widthDiff * self.backSpace / (self.frontSpace+self.backSpace)))