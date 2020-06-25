from pkg.geometry.all import Point
from pkg.pose.all import mpi, Mode
from pkg.errors import Error


class Cache(object):
    def __init__(self, mode: Mode):
        self.points = {}
        self.mode = mode

    def __json__(self):
        return {
            'mode': self.mode,
            'points': self.points,
        }

    def load(self, cacheDict: dict):
        mode = Mode.fromString(cacheDict['mode'])
        if mode != self.mode:
            raise('Cache error: mode mismatches')

        self.__setupCreateModel()
        self.__loadPoints(cacheDict['points'])

    def __setupCreateModel(self):
        if self.mode is Mode.COCO:
            raise Error('COCO cache not available yet')
        elif self.mode is Mode.MPI:
            self.__createModel = self.__createMPIModel

    def __loadPoints(self, framesDict: dict):
        for key, pointDictList in framesDict.items():
            points = []
            for pointDict in pointDictList:
                if pointDict:
                    points.append(Point.loadFromDict(pointDict))
                else:
                    points.append(None)
            
            self.points[int(key)] = self.__createModel(points)


    def __createMPIModel(self, points: list) -> mpi.Model:
        return mpi.Model(points)

    @staticmethod
    def loadFromDict(cacheDict: dict, mode: Mode):
        cache = Cache(mode)
        cache.load(cacheDict)
        return cache
