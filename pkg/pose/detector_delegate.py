import time
import cv2
from .detector import Detector
from pkg.geometry.all import Point
from pkg.graphics.all import Frame


class DetectorDelegate(object):
    def __init__(self, detector: Detector, frame: Frame):
        self.master = detector
        self.frame = frame

    def detect(self) -> list:
        '''Returns detected keypoints list.'''
        inputBlob = cv2.dnn.blobFromImage(
            self.frame.data, 1.0/255,
            (self.master.inWidth, self.master.inHeight),
            (0, 0, 0), swapRB=False, crop=False)

        net = self.master.net
        net.setInput(inputBlob)
        self.output = net.forward()

        return self.__getKeypoints()

    def __getKeypoints(self) -> list:
        self.outWidth = self.output.shape[3]
        self.outHeight = self.output.shape[2]

        points = []
        for i in range(self.master.nPoints):
            points.append(self.__getKeypoint(i))

        return points

    def __getKeypoint(self, i) -> (int, int):
        probMap = self.output[0, i, :, :]

        # Extract point and probability
        _, prob, _, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image.
        x = (self.frame.width * point[0]) / self.outWidth
        y = (self.frame.height * point[1]) / self.outHeight

        if prob > self.master.threshold:
            return Point(int(x), int(y))
        else:
            return None