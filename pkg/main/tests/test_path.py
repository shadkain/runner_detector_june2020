import unittest
from pkg.main.paths import *


class TestPaths(unittest.TestCase):
    def testCOCOCachePath(self):
        testName = 'fake.mov'

        cachePath = pathForCache(testName, Mode.COCO)

        assert cachePath == path.join(cacheDirPath, 'fake.mov.coco.json')

    def testMPICachePath(self):
        testName = 'fake.mov'

        cachePath = pathForCache(testName, Mode.MPI)

        assert cachePath == path.join(cacheDirPath, 'fake.mov.mpi.json')
