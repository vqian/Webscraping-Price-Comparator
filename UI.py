###################
# UI with Tkinter #
###################

from tkinter import *
from webscraping import *

"""
Parameters: Struct data
Sets values for data
"""
def init(data):
    data.inputMode = True
    data.priceResultMode = False

    data.numFields = 4
    data.fieldLabels = ["Brand", "Year", "Model", "Details"]
    data.inputFields = []
    data.inputLabels = []
    data.userInput = []

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
    if data.priceResultMode:
        print(data.priceStatistics)
        namePosition = data.height / 4
        canvas.create_text(data.width / 2, namePosition, text = "".join(data.userInput), font = "Helvetica 20")
        pricesPosition = data.height * 3 / 4
        canvas.create_text(data.width / 2, pricesPosition, text = data.priceStatistics, font = "Helvetica 14")

def getInput(data):
    print("Loading price information...")
    for row in range(data.numFields):
        inputText = data.inputFields[row].get()
        if inputText != "":
            data.userInput.append(inputText)

    data.priceStatistics = searchURLs(data.userInput)
    data.inputMode = False
    data.priceResultMode = True

"""
Parameters: ints width, height for dimensions of canvas in pixels
Part of code from course notes (beginning and end of own code denoted by ***)
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
    root.title("Price Comparator") # name of app
    root.resizable(width = False, height = False)

    init(data)

    """
    ***
    Initialize input textboxes 
    """
    if data.inputMode:
        for row in range(data.numFields):
            inputLabel = Label(root, text =  data.fieldLabels[row])
            data.inputLabels.append(inputLabel)
            data.inputLabels[row].grid(row  = row, column = 0, sticky = "nsew", padx = 2, pady = 2)
            
            fieldName = "input" + str(row)
            fieldName = Entry(root)
            data.inputFields.append(fieldName)
            data.inputFields[row].grid(row  = row, column = 1, sticky = "nsew", padx = 2, pady = 2)
            

        Button(root, text = "Enter", command = lambda: getInput(data)).grid(row = 21, column = 1)
    """
    ***
    """

    canvas = Canvas(root, width = data.width, height = data.height)
    canvas.configure(bd = 0, highlightthickness = 0)
    try:
        canvas.pack()
    except:
        pass

    root.bind("<Button-1>", lambda event:
                mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)

    root.mainloop()

###############
# Run Program #
###############

#run()