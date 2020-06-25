import json
from .names import POINTS_NAMES, Point
from pkg.geometry.point import Point as XYPoint
from pkg.errors import Error


class Model(object):
    N_POINTS = 18

    def __init__(self, keypoints: list):
        if len(keypoints) != self.N_POINTS:
            raise Error(f'Incorrect list length. Expected: {self.N_POINTS}; Actually: {len(keypoints)}')

        self.keypoints = []
        for point in keypoints:
            if point:
                self.keypoints.append(XYPoint(point[0], point[1]))
            else:
                self.keypoints.append(None)

    def __str__(self):
        s = '{'

        for i, point in enumerate(self.keypoints):
            s += f'\n\t"{POINTS_NAMES[i]}": {point}'
        
        return s + '\n}'

    def __json__(self):
        return self.keypoints

    def get(self, point: Point) -> XYPoint:
        return self.keypoints[point]
    