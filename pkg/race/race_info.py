import json
from pkg.geometry.all import Rect, Point, Line


class RaceInfo(object):
    def __init__(self, jsonString: str):
        raceDict = json.loads(jsonString)

        self.distance = raceDict['distance']
        self.startLine = Line.loadFromDict(raceDict['start-line'])
        self.endLine = Line.loadFromDict(raceDict['finish-line'])

        self.startFrame = raceDict.get('start-frame', 0)
        self.initialRect = Rect.loadFromDict(raceDict['initial-rect'])
        self.finishOffset = raceDict['finish-offset']

    @staticmethod
    def loadFromFile(jsonPath: str):
        with open(jsonPath, 'r') as file:
            return RaceInfo(file.read())