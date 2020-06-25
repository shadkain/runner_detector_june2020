import time
from .all import Cache, CacheLoader
from pkg.config.all import Config
from pkg.geometry.all import Rect
from pkg.graphics.all import VideoFrame
from pkg.pose.all import Detector, mpi, Mode
from pkg.errors import Error


class ModelProvider(object):
    def __init__(self, videoName: str, config: Config):
        self.mode = config.mode
        self.useCache = config.useCache
        self.setup(videoName, config.posePath)

    def setup(self, videoName: str, posePath: str) -> mpi.Model:
        self.cache: Cache = None

        if self.useCache:
            st = time.time()
            hasCache, self.cache = CacheLoader().load(videoName, self.mode)
            if hasCache:
                print(f'--- Using cache for "{videoName}". Loading time: {time.time() - st} s')
        
        if not self.cache:
            self.cache = Cache(self.mode)
            self.detector = Detector(posePath, self.mode)
            self.useCache = False

    def provide(self, frame: VideoFrame, searchRect: Rect):
        # Return cached results if exists
        if self.useCache:
            return self.cache.points.get(frame.position, None)

        # Crop frame within search area rect
        croppedFrame = frame.crop(searchRect)
        keypoints, time = self.detector.detect(croppedFrame)
        print(f'Frame: {frame.position}, detecting time: {time} s')

        # Transform resulting points to fit original frame
        for point in keypoints:
            if point:
                point.x = point.x + croppedFrame.rect.minX
                point.y = point.y + croppedFrame.rect.minY

        if self.mode is Mode.MPI:
            model = mpi.Model(keypoints)
            self.cache.points[frame.position] = model
            return model
        else:
            raise Error('Unsupported mode')
