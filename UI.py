###################
# UI with Tkinter #
###################

from tkinter import *
from UserInput import UserInput

def getUserInput(prompt):
    inputBox = UserInput(prompt)
    inputBox.waitForInput()
    return inputBox.getInput()

"""
Parameters: Struct data
Sets values for data
"""
def init(data):
    userInput = getUserInput("Please enter item name")
    data.userInput = userInput
    print(data.userInput)

"""
Parameters: event variable holding data captured by event loop, Struct data
Tracks and responds to mouse clicks
"""
def mousePressed(event, data):
    pass

"""
Parameters: event variable holding data captured by event loop, Struct data
Tracks and responds to keyboard presses
"""
def keyPressed(event, data):
    pass

"""
Parameters: graphics canvas, Struct data
"""
def redrawAll(canvas, data):
    canvas.create_text(0, 0, text = data.userInput, font = "Helvetica 12 bold", 
                        fill = "black")

"""
Parameters: ints width, height for dimensions of canvas in pixels
Code from course notes
"""
def run(width = 600, height = 600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill = 'white', width = 0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.title("Price Comparator") # custom name of app
    root.resizable(width = False, height = False)

    init(data)

    canvas = Canvas(root, width = data.width, height = data.height)
    canvas.configure(bd = 0, highlightthickness = 0)
    canvas.pack()

    root.bind("<Button-1>", lambda event:
                mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)

    root.mainloop()

###############
# Run Program #
###############

run()