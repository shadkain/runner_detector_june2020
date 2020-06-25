import json
from .all import RaceConfig, ViewConfig
from pkg.pose.all import Mode
from pkg.graphics.all import colorFromString as cfs


class Config(object):
    def __init__(self, configDict: dict):
        self.mode = Mode.fromString(configDict['mode'])
        self.useCache = configDict['use-cache']
        self.posePath = configDict['pose-path']
        self.race = RaceConfig(configDict['race'])
        self.colors = ViewConfig(configDict['view'])

    @staticmethod
    def loadFromFile(path: str):
        with open(path, 'r') as file:
            configDict = json.loads(file.read())
            return Config(configDict)