from tkinter import *

class UserInput(object):
    def __init__(self, prompt):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.allowInput(prompt)
        self.input = ""

    def getText(self):
        self.input = self.inputLabel.get()
        self.root.destroy()

    def allowInput(self, prompt):
        frame1 = self.frame

        inputLabel = Label(frame1, text = prompt)
        inputLabel.pack(side = "left")
        self.inputLabel = Entry(frame1, text = "Item Name")
        self.inputLabel.pack(side = "left")
        self.inputLabel.focus_set()
        enterButton = Button(frame1, text = "Enter", command = self.getText)
        enterButton.pack(side = "right")

    def getInput(self):
        return self.input

    def waitForInput(self):
        self.root.mainloop()