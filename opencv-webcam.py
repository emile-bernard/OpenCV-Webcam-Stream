import cv2
import sys

video_capture = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")

def drawRectagle(frame):
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

def releaseCapture():
    video_capture.release()
    cv2.destroyAllWindows()

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    drawRectagle(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

releaseCapture()