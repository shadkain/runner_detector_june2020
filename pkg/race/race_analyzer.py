from pkg.main.all import RaceInfo
from pkg.config.config import RaceConfig


class RaceAnalyzer(object):
    def __init__(self, raceInfo: RaceInfo, config: RaceConfig):
        self.raceInfo = raceInfo
        self.config = config