from tkinter import *
from webscraping import *
from UI import *
import webbrowser

class PriceComparator(object):
    def __init__(self):
        self.numFields = 4
        self.fieldLabels = ["Brand", "Year", "Model", "Details"]
        self.inputFields = []
        self.inputLabels = []
        self.userInput = []
        self.inputMode = True
        self.priceResultMode = False
        self.run()

    def run(self, width = 600, height = 600):
        class Struct(object): pass
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Price Comparator") # name of app
        self.root.resizable(width = False, height = False)

        self.drawInputScreen()
        #self.drawPriceResultScreen()
        self.root.mainloop()

    def getInput(self):
        if self.inputMode:
            print("Loading price information...")
            for row in range(self.numFields):
                inputText = self.inputFields[row].get()
                if inputText != "":
                    self.userInput.append(inputText)

            self.priceStatistics = searchURLs(self.userInput)
        self.inputMode = False
        self.priceResultMode = True
        drawPriceResultScreen()

    def drawInputScreen(self):
        for row in range(self.numFields):
            inputLabel = Label(self.root, text = self.fieldLabels[row])
            self.inputLabels.append(inputLabel)
            self.inputLabels[row].grid(row  = row, column = 0, sticky = "nsew", padx = 2, pady = 2)
              
            fieldName = "input" + str(row)
            fieldName = Entry(self.root)
            self.inputFields.append(fieldName)
            self.inputFields[row].grid(row  = row, column = 1, sticky = "nsew", padx = 2, pady = 2)

        Button(self.root, text = "Enter", command = lambda: getInput).grid(row = 21, column = 1)

    def callback(event):
        webbrowser.open_new(r"http://www.google.com")

    def drawPriceResultScreen(self):
        if self.priceResultMode:
            self.name = "".join(self.userInput)
            print(name)
            print(self.priceStatistics)
            namePosition = self.height / 4

            self.canvas = Canvas(self.root, width = self.width, height = self.height)
            self.canvas.configure(bd = 0, highlightthickness = 0)

            self.canvas.create_text(self.width / 2, namePosition, text = self.name, font = "Helvetica 20")
            pricesPosition = self.height * 3 / 4
            self.canvas.create_text(self.width / 2, pricesPosition, text = self.priceStatistics, font = "Helvetica 14")
            """
            urls = getURLs(self.userInput)
            for i in range(len(urls)):
                link = Label(self.root, text = "Hyperlink: " + urls[i], fg = "blue", cursor = "hand2")
                link.pack()
                link.bind("<Button-" + str(i + 1) + ">", callback)
            """