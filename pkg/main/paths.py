from os import path
from pkg.pose.all import Mode


inputPath = 'input'
videoDirPath = path.join(inputPath, 'video')
raceInfoPath = path.join(inputPath, 'info')
cacheDirPath = path.join(inputPath, 'cache')

outputPath = 'output'


def pathForOutputVideo(name: str):
    nameWithoutExtension = name.split('.')[0]
    return path.join(outputPath, f'{nameWithoutExtension}.avi')


def pathForVideo(name: str):
    return path.join(videoDirPath, name)


def pathForRaceInfo(name: str):
    return path.join(raceInfoPath, f'{name}.json')


def pathForCache(name: str, mode: Mode):
    return path.join(cacheDirPath, f'{name}.{mode.lower}.json')


def pathForGzippedCache(name: str, mode: Mode):
    return f'{pathForCache(name, mode)}.gz'
    
