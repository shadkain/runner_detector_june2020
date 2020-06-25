import time
from .all import Loader, Mode
from pkg.graphics.frame import Frame


class Detector(object):
    def __init__(self, posePath='pose', mode=Mode.MPI):
        loader = Loader(posePath, mode)

        self.net, self.nPoints = loader.loadNet()
        self.__setup()

    def __setup(self):
        self.inWidth = 368
        self.inHeight = 368
        self.threshold = 0.1

    def detect(self, frame: Frame) -> (list, float):
        '''Returns detected keypoints list, detecting time in seconds.'''
        from .detector_delegate import DetectorDelegate
        
        startTime = time.time()

        delegate = DetectorDelegate(self, frame)
        return delegate.detect(), time.time()-startTime
        