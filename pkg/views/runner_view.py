import enum
from pkg.pose.all import mpi
from pkg.graphics.all import Frame, Color, Drawable


class DrawingMode(enum.Enum):
    POINTS = enum.auto()
    SKELETON = enum.auto()
    POINTS_AND_SKELETON = enum.auto()
    NONE = enum.auto()

    @staticmethod
    def load(showPoints: bool, showSkeleton: bool):
        if showPoints and showSkeleton:
            return DrawingMode.POINTS_AND_SKELETON
        elif showPoints:
            return DrawingMode.POINTS
        elif showSkeleton:
            return DrawingMode.SKELETON
        else:
            return DrawingMode.NONE


class RunnerView(Drawable):
    def __init__(self, pointsColor=Color.red(), skeletonColor=Color.yellow(), drawingMode=DrawingMode.POINTS_AND_SKELETON):
        super().__init__()
        self.drawingMode = drawingMode
        self.pointsColor = pointsColor
        self.skeletonColor = skeletonColor
        self.update(None)

    def update(self, model: mpi.Model):
        self.model = model
    
    def draw(self, frame: Frame):
        drawPoints, drawSkeleton = self.__shouldDraw()

        if drawPoints:
            self.__drawPoints(frame)
        if drawSkeleton:
            self.__drawSkeleton(frame)

    def __shouldDraw(self) -> (bool, bool):
        if self.drawingMode is DrawingMode.NONE or not self.model:
            return False, False
        if self.drawingMode is DrawingMode.POINTS:
            return True, False
        if self.drawingMode is DrawingMode.SKELETON:
            return False, True
        if self.drawingMode is DrawingMode.POINTS_AND_SKELETON:
            return True, True
    
    def __drawPoints(self, frame: Frame):
        for point in self.model.keypoints:
            if point:
                frame.drawCircle(point, 3, self.pointsColor)

    def __drawSkeleton(self, frame: Frame):
        for pair in self.model.pairs:
            frame.drawLineByPoints(pair[0], pair[1], 2, self.skeletonColor)


assert issubclass(RunnerView, Drawable)