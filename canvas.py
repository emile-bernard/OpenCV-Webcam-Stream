import tkinter as tk

class Canvas:
    def __init__(self, parent, videoCapture):
        self.canvas = tk.Canvas(parent, width = videoCapture.getWidth(), height = videoCapture.getHeight())
        self.draw()

    def draw(self):
        self.canvas.pack()

    def createImage(self, x, y, image, anchor):
        self.canvas.create_image(x, y, image = image, anchor = anchor)
