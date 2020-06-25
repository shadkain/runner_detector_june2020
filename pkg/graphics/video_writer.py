import cv2
from .all import Frame


class VideoWriter(object):
    def __init__(self, filename: str, fps: float, width: int, height: int):
        self.writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))

    def write(self, frame: Frame):
        self.writer.write(frame.data)

    def release(self):
        self.writer.release()