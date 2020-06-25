import cv2
from .all import VideoFrame
from pkg.errors import Error


class Video(object):
    def __init__(self, path: str):
        self.cap = cv2.VideoCapture(path)
        if not self.cap:
            raise Error(f'Video by path: "{path}" cannot be opened')

    @property
    def width(self) -> int:
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    @property
    def height(self) -> int:
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    @property
    def fps(self) -> int:
        return int(self.cap.get(cv2.CAP_PROP_FPS))

    @property
    def framePosition(self) -> int:
        return int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))

    @framePosition.setter
    def framePosition(self, value):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, value)

    def forward(self) -> bool:
        hasData, data = self.cap.read()
        if hasData:
            self.frame = VideoFrame(data, self.framePosition-1)

        return hasData