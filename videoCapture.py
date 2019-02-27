import cv2

class VideoCapture:
    def __init__(self, videoPath):
        self.videoCapture = cv2.VideoCapture(videoPath)
        self.width = self.videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.videoCapture.isOpened():
            self.videoCapture.release()

    def getFrame(self):
        if self.videoCapture.isOpened():
            isFrameRead, frame = self.videoCapture.read()
            if isFrameRead:
                 return (isFrameRead, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isFrameRead, None)
        else:
            return (isFrameRead, None)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setVideoPath(self, videoPath):
        self.videoCapture = cv2.VideoCapture(videoPath)
