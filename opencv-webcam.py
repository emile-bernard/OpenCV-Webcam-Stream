import cv2
import sys

videoCapture = cv2.VideoCapture(0)
pretrainedFaceClassifier = cv2.CascadeClassifier("./assets/model/haarcascade_frontalface_alt.xml")

def drawText(frame, text, position):
    font = cv2.FONT_HERSHEY_DUPLEX
    scale = 1
    color = (255, 255, 255)
    thickness = 1
    cv2.putText(frame, text, position, font, scale, color, thickness)

def drawDetectedObjects(frame, objects):
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        drawText(videoFrame, "Face", (x, y-10))

def releaseCapture():
    videoCapture.release()
    cv2.destroyAllWindows()

while True:
    returnValue, videoFrame = videoCapture.read()
    colorSpace = cv2.cvtColor(videoFrame, cv2.COLOR_BGR2GRAY)
    detectedObjects = pretrainedFaceClassifier.detectMultiScale(
        colorSpace,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    drawDetectedObjects(videoFrame, detectedObjects)


    cv2.imshow('OpenCV face recogniton applied to a webcam video stream', videoFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

releaseCapture()
