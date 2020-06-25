import os, time
import cv2
from .mode import Mode
from pkg.errors import Error


class Loader(object):
    def __init__(self, posePath: str, mode: Mode):
        self.posePath = posePath
        self.mode = mode

    def loadNet(self) -> (any, int):
        mode = self.mode

        if mode is Mode.COCO:
            return self.__loadCOCONet()
        elif mode is Mode.MPI:
            return self.__loadMPINet()

    def __loadCOCONet(self):
        return self.__loadNet(
            prototxt='coco/pose_deploy_linevec.prototxt',
            caffemodel='coco/pose_iter_440000.caffemodel'
        ), 18

    def __loadMPINet(self):
        return self.__loadNet(
            prototxt='mpi/pose_deploy_linevec_faster_4_stages.prototxt',
            caffemodel='mpi/pose_iter_160000.caffemodel'
        ), 15

    def __loadNet(self, prototxt: str, caffemodel: str):
        prototxtPath = os.path.join(self.posePath, prototxt)
        caffemodelPath = os.path.join(self.posePath, caffemodel)

        startTime = time.time() 
        net = cv2.dnn.readNetFromCaffe(prototxtPath, caffemodelPath)
        print(f'--- Model "{self.mode}" loaded. Loading time: {(time.time() - startTime):5.4} s')

        return net