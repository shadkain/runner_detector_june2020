from pkg.graphics.all import Window, Video, VideoFrame, VideoWriter


class VideoWindow(Window):
    def __init__(self, name: str, videoPath: str):
        super().__init__(name)

        self.video = Video(videoPath)
        self.__onForward = None

    def createVideoWriter(self, filename: str) -> VideoWriter:
        return VideoWriter(filename, self.video.fps, self.video.width, self.video.height)

    @property
    def frame(self) -> VideoFrame:
        return self.video.frame

    def forward(self) -> bool:
        return self.video.forward()


assert issubclass(VideoWindow, Window)
