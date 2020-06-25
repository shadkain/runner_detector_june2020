import os, json, gzip
from pkg.pose.all import Mode
from pkg.json.encoder import Encoder
from .all import *


class CacheLoader(object):
    def load(self, name: str, mode: Mode) -> (bool, Cache):
        '''Loads cache for name from disk.'''
        # Check for non-gzipped cache
        path = pathForCache(name, mode)
        print(path)
        if os.path.isfile(path):
            with open(path, 'r') as file:
                return True, self.__load(file.read(), mode)
        
        # Check for gzipped cache
        path = pathForGzippedCache(name, mode)
        if os.path.isfile(path):
            with gzip.open(path, 'r') as file:
                return True, self.__load(file.read(), mode)

        return False, None
                
    
    def __load(self, contents: str, mode: Mode) -> Cache:
        cacheDict = json.loads(contents)
        return Cache.loadFromDict(cacheDict, mode)

