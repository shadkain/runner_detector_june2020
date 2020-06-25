import json
from .mpi import Point, POINTS_NAMES, POINT_PAIRS
from pkg.geometry.all import Point as XYPoint
from pkg.errors import Error


class Model(object):
    N_POINTS = 15

    def __init__(self, keypoints: list):
        if len(keypoints) != self.N_POINTS:
            raise Error(f'Incorrect list length. Expected: {self.N_POINTS}; Actually: {len(keypoints)}')

        self.keypoints = keypoints

    def __str__(self):
        s = '{'

        for i, point in enumerate(self.keypoints):
            s += f'\n\t"{POINTS_NAMES[i]}": {point}'
        
        return s + '\n}'

    def __json__(self):
        return self.keypoints

    def get(self, point: Point) -> XYPoint:
        return self.keypoints[point]

    @property
    def pairs(self) -> list:
        pairs = []

        for pair in POINT_PAIRS:
            begin = self.get(pair[0])
            end = self.get(pair[1])

            if begin and end:
                pairs.append((begin, end))

        return pairs