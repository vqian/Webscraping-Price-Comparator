from tkinter import *
from webscraping import *
from UI import *

class PriceComparator(object):
    def __init__(self):
        self.numFields = 4
        self.fieldLabels = ["Brand", "Year", "Model", "Details"]
        self.inputFields = []
        self.inputLabels = []
        self.userInput = []
        self.run()

    def run(self, width = 600, height = 600):
        class Struct(object): pass
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Price Comparator") # name of app
        self.root.resizable(width = False, height = False)

        self.drawInputScreen()
        self.root.mainloop()

    def getInput(self):
        print("Loading price information...")
        for row in range(self.numFields):
            inputText = self.inputFields[row].get()
            if inputText != "":
                self.userInput.append(inputText)

        self.priceStatistics = searchURLs(self.userInput)
        drawPriceResultScreen()

    def drawInputScreen(self):
        for row in range(self.numFields):
            inputLabel = Label(root, text = self.fieldLabels[row])
            self.inputLabels.append(inputLabel)
            self.inputLabels[row].grid(row  = row, column = 0, sticky = "nsew", padx = 2, pady = 2)
              
            fieldName = "input" + str(row)
            fieldName = Entry(self.root)
            self.inputFields.append(fieldName)
            self.inputFields[row].grid(row  = row, column = 1, sticky = "nsew", padx = 2, pady = 2)

        Button(self.root, text = "Enter", command = lambda: getInput).grid(row = 21, column = 1)

    def drawPriceResultScreen(self):
        print(self.priceStatistics)
        namePosition = self.height / 4
        self.canvas.create_text(self.width / 2, namePosition, text = "".join(self.userInput), font = "Helvetica 20")
        pricesPosition = self.height * 3 / 4
        self.canvas.create_text(self.width / 2, pricesPosition, text = self.priceStatistics, font = "Helvetica 14")