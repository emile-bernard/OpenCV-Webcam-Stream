import tkinter as tk
from model import Model

class ModelListBox:
    LISTBOX_WIDTH = 30
    LISTBOX_HEIGHT = 30

    def __init__(self, parent, model, modelFiles):
        self.modelListBox = tk.Listbox(parent)
        self.model = model
        self.modelFiles = modelFiles
        self.draw()

    def draw(self):
        self.modelListBox.config(width = self.LISTBOX_WIDTH, height = self.LISTBOX_HEIGHT)

        for modelFile in self.modelFiles:
            self.modelListBox.insert(tk.END, modelFile[0])

        self.modelListBox.bind('<<ListboxSelect>>', self.modelListBoxSelectionChanged)
        self.modelListBox.select_set(0) #Sets focus on the first item.
        self.modelListBox.event_generate("<<ListboxSelect>>")
        self.modelListBox.pack(side = "left")

    def modelListBoxSelectionChanged(self, *args):
        isSelectedPath, selectedModelPath = self.getSelectedModelPath()
        if(isSelectedPath):
            self.model.setModelClassifierPath(self.getSelectedModelName(), selectedModelPath)

    def getSelectedModelPath(self):
        try:
            curentSelection = self.modelListBox.curselection()[0]
            return (True, self.modelFiles[curentSelection][1])
        except:
            return (False, None)

    def getSelectedModelName(self):
        curentSelection = self.modelListBox.curselection()[0]
        return self.modelFiles[curentSelection][0]
