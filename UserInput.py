from tkinter import *

class UserInput(object):
    def __init__(self, prompt):
        self.root = Tk()
        self.string = ""
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(prompt)

    def acceptInput(self, prompt):
        r = self.frame

        k = Label(r, text = prompt)
        k.pack(side = "left")
        self.e = Entry(r, text = "Item Name")
        self.e.pack(side = "left")
        self.e.focus_set()
        b = Button(r, text = "Enter", command = self.getText)
        b.pack(side = "right")

    def getText(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()