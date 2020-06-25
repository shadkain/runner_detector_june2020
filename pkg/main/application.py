import cv2
import time
from .all import *
from pkg.config.all import Config
from pkg.pose.all import Mode, mpi
from pkg.geometry.all import boundingRect
from pkg.graphics.all import VideoWindow, VideoFrame, Color
from pkg.views.all import *
import json
from pkg.json.encoder import Encoder
import gzip


class Application(object):
    def __init__(self, videoName: str, config: Config):
        self.videoName = videoName
        self.config = config
        self.modelProvider = ModelProvider(videoName, config)

        self.raceInfo = RaceInfo.loadFromFile(pathForRaceInfo(videoName))
        self.searchRect = self.raceInfo.initialRect.copy()

        self.tracker = Tracker(1, 2)

        self.window = VideoWindow('Race', pathForVideo(videoName))
        self.view = ApplicationView(self.window, self.raceInfo, config.colors)

        self.videoWriter = self.window.createVideoWriter(pathForOutputVideo(videoName))


    def run(self):
        self.startFrame = None
        self.finishFrame = None

        while self.window.forward():
            startTime = time.time()

            self.tick(self.window.frame)
            self.videoWriter.write(self.window.frame)

            elapsed = time.time() - startTime
            if elapsed < 0.1:
                time.sleep(0.1 - elapsed)
            self.window.waitKey()
        
        self.window.waitKey()
        self.videoWriter.release()
        if not self.modelProvider.useCache:
            with open(pathForCache(self.videoName, self.modelProvider.mode), 'w') as file:
                data = json.dumps(self.modelProvider.cache, cls=Encoder)
                file.write(data)
        
    def tick(self, frame: VideoFrame):
        if frame.position >= self.raceInfo.startFrame:
            if not self.finishFrame or (frame.position - self.finishFrame) <= self.raceInfo.finishOffset:
                model = self.modelProvider.provide(frame, self.searchRect)
            else:
                model = None
                time = (self.finishFrame-self.startFrame)/120
                d = 5.0
                v = d / time
                cv2.putText(frame.data, format(v, '.2f')+' m/sec', (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
                cv2.putText(frame.data, format(time, '.2f')+' sec', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
        else:
            model = None

        if model:
            runnerRect = boundingRect(model.keypoints)
            self.view.update(model, runnerRect, self.searchRect)
            self.tracker.track(self.searchRect, runnerRect)
            pos = model.get(mpi.Point.NECK)
            if pos and pos.x >= self.view.trackView.startLine.mid.x and not self.startFrame:
                self.startFrame = frame.position
            if pos and pos.x >= self.view.trackView.endLine.mid.x and not self.finishFrame:
                self.finishFrame = frame.position
            if self.startFrame:
                if not self.finishFrame:
                    time = (frame.position-self.startFrame)/120
                    d = (pos.x - self.raceInfo.startLine.mid.x) / (self.raceInfo.endLine.mid.x - self.raceInfo.startLine.mid.x) * 5
                    if time > 0:
                        v = d / time
                        cv2.putText(frame.data, format(v, '.2f')+' m/sec', (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
                    cv2.putText(frame.data, format(time, '.2f')+' sec', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
                else:
                    time = (self.finishFrame-self.startFrame)/120
                    d = 5.0
                    v = d / time
                    cv2.putText(frame.data, format(v, '.2f')+' m/sec', (50, 100), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
                    cv2.putText(frame.data, format(time, '.2f')+' sec', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
            else:
                cv2.putText(frame.data, f'0.00 sec', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, Color.red().bgr, 2, lineType=cv2.LINE_AA)
        else:
            self.view.setNoModel()
            
        self.window.draw()
        self.window.show()
