import cv2

class Text:
    TEXT_FONT = cv2.FONT_HERSHEY_DUPLEX
    TEXT_COLOR = (255, 255, 255)
    TEXT_SCALE = 0.5
    TEXT_THICKNESS = 1

    def __init__(self, frame, text, position):
        self.frame = frame
        self.position = position
        self.text = text
        self.draw()

    def draw(self):
        cv2.putText(self.frame, self.text, self.position, self.TEXT_FONT, self.TEXT_SCALE, self.TEXT_COLOR, self.TEXT_THICKNESS)
