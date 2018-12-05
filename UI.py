###################
# UI with Tkinter #
###################

from tkinter import *
from webscraping import *
from PriceResults import *
import webbrowser
from PriceGraph import *
from CachedResults import *

"""
Parameters: Struct data
Sets values for data
"""
def init(data):
    data.numFields = 4
    data.fieldLabels = ["Brand", "Year", "Model", "Details"]
    data.inputFields = []
    data.inputLabels = []
    data.userInput = []
    data.images = []

    data.inputMode = True
    data.priceResultMode = False
    data.priceGraphMode = False

    data.year = 2018

    data.buttonSize = (40, 20)
    data.inputButton = (10, 10)
    data.graphButton = (data.width - 10 - data.buttonSize[0], 10)

    data.root = Tk() 

    data.cachedResults = CachedResults()

def inRegion(event, leftTop, buttonSize):
    left, top = leftTop
    width, height = buttonSize
    right = left + width
    bottom = top + height
    x, y = event.x, event.y
    
    return x >= left and x <= right and y >= top and y <= bottom

"""
Parameters: event variable holding data captured by event loop, Struct data
Tracks and responds to mouse clicks
"""
def mousePressed(event, data):
    if data.priceResultMode:
        if inRegion(event, data.inputButton, data.buttonSize):
            data.inputMode = True
            data.priceResultMode = False
            data.priceGraphMode = False
        elif inRegion(event, data.graphButton, data.buttonSize):
            data.inputMode = False
            data.priceResultMode = False
            data.priceGraphMode = True
    """
    elif data.priceGraphMode:
        if inRegion(event, data.inputButton, data.buttonSize):
            data.inputMode = True
            data.priceResultMode = False
            data.priceGraphMode = False
        elif inRegion(event, data.graphButton, data.buttonSize):
            data.inputMode = False
            data.priceResultMode = False
            data.priceGraphMode = True
    """

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
    if data.inputMode:
        drawInputScreen(canvas, data)
    elif data.priceResultMode:
        drawPriceResultScreen(canvas, data)
    elif data.priceGraphMode:
        drawPriceGraphScreen(canvas, data)

def getInput(data):
    print("Loading price information...")
    for row in range(data.numFields):
        inputText = data.inputFields[row].get()
        if inputText != "":
            data.userInput.append(inputText)
            if row == 1 and (type(int(inputText)) == int):
                data.year = int(inputText)

    data.priceStatistics, data.averagePrices = None, None
    name = " ".join(data.userInput)
    if data.cachedResults.isCached(name):
        print("Matched previously searched entity: loading data...")
        data.priceStatistics, data.averagePrices = data.cachedResults.getCachedPriceStatistics(data.userInput)
    else:
        print("No matched previously searched entity: loading data...")
        data.priceStatistics, data.averagePrices, data.images = searchURLs(data.userInput)
        data.cachedResults.cacheResults(name, data.priceStatistics, data.averagePrices, data.images)

    data.inputMode = False
    data.priceResultMode = True
    data.priceGraphMode = True

    #drawPriceResultScreen(data)
    #drawPriceGraphScreen(data)

def drawInputScreen(canvas, data):
    for row in range(data.numFields):
        inputLabel = Label(data.root, text = data.fieldLabels[row])
        data.inputLabels.append(inputLabel)
        data.inputLabels[row].grid(row  = row, column = 0, sticky = "nsew", padx = 2, pady = 2)
                  
        fieldName = "input" + str(row)
        fieldName = Entry(data.root)
        data.inputFields.append(fieldName)
        data.inputFields[row].grid(row  = row, column = 1, sticky = "nsew", padx = 2, pady = 2)

    Button(data.root, text = "Enter", command = lambda: getInput(data)).grid(row = 21, column = 1)

def drawPriceResultScreen(canvas, data):
    #pr = PriceResults()
    pr = PriceResults(canvas)
    pr.priceResultMode = data.priceResultMode
    pr.userInput = data.userInput
    pr.priceStatistics = data.priceStatistics
    pr.images = data.images

    pr.buttonSize = data.buttonSize
    pr.inputButton = data.inputButton
    pr.graphButton = data.graphButton
    #pr.run()
    pr.drawPriceResultScreen()

def drawPriceGraphScreen(canvas, data):
    print("Loading graph...")
    p = PriceGraph()

    numYears = 3
    startYear = data.year - (numYears - 1)
    endYear = data.year + (numYears  - 1)
    if endYear > 2018:
        endYear = 2018
    p.setNumPoints(endYear - startYear + 1)

    for i in range(p.getNumPoints()):
        searchYear = startYear + i
        p.appendYear(searchYear)
        if startYear + i == data.year:
            amazonPrice, ebayPrice, walmartPrice = data.averagePrices
            p.appendPrice(0, amazonPrice)
            p.appendPrice(1, ebayPrice)
            p.appendPrice(2, walmartPrice)
        else:
            searchInput = data.userInput
            searchInput[1] = str(searchYear)
            priceStatistics, averagePrices, images = searchURLs(searchInput)
            amazonPrice, ebayPrice, walmartPrice = averagePrices
            p.appendPrice(0, amazonPrice)
            p.appendPrice(1, ebayPrice)
            p.appendPrice(2, walmartPrice)

    p.graphFromPoints()

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

run()