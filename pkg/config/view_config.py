from pkg.graphics.all import colorFromString as cfs

class ViewConfig(object):
    def __init__(self, viewDict: dict):
        # Track
        self.showTrack, self.trackColor = self.__showColor(viewDict['track'])

        # Runner
        runnerDict = viewDict['runner']
        self.showRunnerPoints, self.runnerPointsColor = self.__showColor(runnerDict['points'])
        self.showRunnerSkeleton, self.runnerSkeletonColor = self.__showColor(runnerDict['skeleton'])
        self.showRunnerRect, self.runnerRectColor = self.__showColor(runnerDict['rect'])

        # Tracking rect
        self.showTrackingRect, self.trackingRectColor = self.__showColor(viewDict['tracking-rect'])

    def __showColor(self, showColorDict: dict):
        return showColorDict['show'], cfs(showColorDict['color'])
    