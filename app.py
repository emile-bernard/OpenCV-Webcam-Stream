import re
import os
import cv2
import sys
import time
import tkinter as tk
import PIL.Image, PIL.ImageTk

from model import Model
from videoCapture import VideoCapture
from modelListBox import ModelListBox
from canvas import Canvas

class App(tk.Frame):
    UPDATE_DELAY = 15

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.modelFiles = self.getFiles("./assets/models")
        self.model = Model(self.modelFiles[0][0], self.modelFiles[0][1])
        self.videoCapture = VideoCapture(0)

        self.modelListBox = ModelListBox(self.parent, self.model, self.modelFiles)
        self.canvas = Canvas(self.parent, self.videoCapture)
        self.update()

    def getFiles(self, path):
        assetFiles = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                assetFileName = re.search(r'haarcascade_(.*?).xml', filename).group(1)
                assetFilePath = os.path.join(root, filename)
                assetFile = (assetFileName, assetFilePath)
                assetFiles.append(assetFile)
        return assetFiles

    def update(self):
        isFrameRead, frame = self.videoCapture.getFrame()
        if isFrameRead:
            self.model.detectObjects(frame)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.createImage(0, 0, self.photo, tk.NW)
        self.parent.after(self.UPDATE_DELAY, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OpenCV Webcam")
    root.resizable(0, 0)
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
