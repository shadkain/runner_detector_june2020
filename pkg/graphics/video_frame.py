from .all import Frame


class VideoFrame(Frame):
    def __init__(self, data, position: int):
        super().__init__(data)
        self.__position = position

    @property
    def position(self) -> int:
        return self.__position