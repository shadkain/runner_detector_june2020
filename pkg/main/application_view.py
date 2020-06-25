from pkg.views.all import *
from pkg.geometry.all import Rect
from pkg.graphics.all import VideoWindow
from pkg.race.all import RaceInfo
from pkg.config.all import ViewConfig


class ApplicationView(object):
    def __init__(self, window: VideoWindow, raceInfo: RaceInfo, viewConfig: ViewConfig):
        self.window = window
        
        self.trackView = TrackView(raceInfo.startLine, raceInfo.endLine, viewConfig.trackColor)
        self.trackView.isHidden = not viewConfig.showTrack

        self.runnerView = RunnerView(viewConfig.runnerPointsColor, viewConfig.runnerSkeletonColor,
            DrawingMode.load(viewConfig.showRunnerPoints, viewConfig.showRunnerSkeleton))

        self.runnerRectView = RectView(color=viewConfig.runnerRectColor)
        self.runnerRectView.isHidden = not viewConfig.showRunnerRect

        self.trackingRectView = RectView(raceInfo.initialRect, viewConfig.trackingRectColor)
        self.trackingRectView.isHidden = not viewConfig.showTrackingRect

        for view in [self.trackView, self.runnerRectView, self.runnerView, self.trackingRectView]:
            self.window.addChild(view)

    def update(self, model, runnerRect: Rect, trackingRect: Rect):
        self.runnerView.update(model)
        self.runnerRectView.update(runnerRect)
        self.trackingRectView.update(trackingRect) 

    def setNoModel(self):
        for view in [self.runnerView, self.runnerRectView, self.trackingRectView]:
            view.update(None)
