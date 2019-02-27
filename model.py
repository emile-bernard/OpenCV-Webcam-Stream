import cv2

from rectangle import Rectangle
from text import Text

class Model:
    OBJECT_MIN_HORIZONTAL_SIZE = 20
    OBJECT_MIN_VERTICAL_SIZE = 20

    def __init__(self, classifierPath):
        self.classifier = cv2.CascadeClassifier(classifierPath)
        self.imageScaleFactor = 1.1
        self.canditateRectangleMinNeighbors = 3

    def detectObjects(self, frame):
        colorSpace = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedObjects = self.classifier.detectMultiScale(
            colorSpace,
            scaleFactor = self.imageScaleFactor,
            minNeighbors = self.canditateRectangleMinNeighbors,
            minSize = (self.OBJECT_MIN_HORIZONTAL_SIZE, self.OBJECT_MIN_VERTICAL_SIZE),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        self.drawDetectedObjects(frame, detectedObjects)

    def drawDetectedObjects(self, frame, objects):
        for (x, y, w, h) in objects:
            rectangle = Rectangle(frame, (x, y), (x+w, y+h))
            rectangle.draw()
            text = Text(frame, "Object", (x, y))
            text.draw()

    def setModelClassifierPath(self, modelClassifierPath):
        self.classifier = cv2.CascadeClassifier(modelClassifierPath)
