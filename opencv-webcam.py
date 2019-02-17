import cv2
import sys

videoCapture = cv2.VideoCapture(0)
pretrainedFaceClassifier = cv2.CascadeClassifier("./assets/model/haarcascade_frontalface_alt.xml")

def drawRectagle(frame, objects):
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

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
    drawRectagle(videoFrame, detectedObjects)
    cv2.imshow('OpenCV face recogniton applied to a webcam video stream', videoFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

releaseCapture()
