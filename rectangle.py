import cv2

class Rectangle:
    RECTANGLE_COLOR = (0, 255, 0)
    RECTANGLE_THICKNESS = 1

    def __init__(self, frame, rectangleVertex, rectangleOppositeVertex):
        self.frame = frame
        self.rectangleVertex = rectangleVertex
        self.rectangleOppositeVertex = rectangleOppositeVertex
        self.draw()

    def draw(self):
        cv2.rectangle(self.frame, self.rectangleVertex, self.rectangleOppositeVertex, self.RECTANGLE_COLOR, self.RECTANGLE_THICKNESS)
