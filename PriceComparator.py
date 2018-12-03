from tkinter import *
from webscraping import *
from PriceResults import *
import webbrowser
from PriceGraph import *
from CachedResults import *

class PriceComparator(object):
    cachedResults = CachedResults()

    def __init__(self):
        self.numFields = 4
        self.fieldLabels = ["Brand", "Year", "Model", "Details"]
        self.inputFields = []
        self.inputLabels = []
        self.userInput = []

        self.inputMode = True
        self.priceResultMode = False
        self.priceGraphMode = False

        self.year = 2018
        #self.run()

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
        if self.inputMode:
            print("Loading price information...")
            for row in range(self.numFields):
                inputText = self.inputFields[row].get()
                if inputText != "":
                    self.userInput.append(inputText)
                    if row == 1 and (type(int(inputText)) == int):
                        self.year = int(inputText)

            self.priceStatistics, self.averagePrices = None, None
            name = " ".join(self.userInput)
            if PriceComparator.cachedResults.isCached(name):
                print("Matched previously searched entity: loading data...")
                self.priceStatistics, self.averagePrices = PriceComparator.cachedResults.getCachedPriceStatistics(self.userInput)
            else:
                print("No matched previously searched entity: loading data...")
                self.priceStatistics, self.averagePrices = searchURLs(self.userInput)
                PriceComparator.cachedResults.cacheResults(name, self.priceStatistics, self.averagePrices)

            self.inputMode = False
            self.priceResultMode = True
            self.priceGraphMode = True

            self.drawPriceResultScreen()
            self.drawPriceGraphScreen()

    def drawInputScreen(self):
        if self.inputMode:
            for row in range(self.numFields):
                inputLabel = Label(self.root, text = self.fieldLabels[row])
                self.inputLabels.append(inputLabel)
                self.inputLabels[row].grid(row  = row, column = 0, sticky = "nsew", padx = 2, pady = 2)
                  
                fieldName = "input" + str(row)
                fieldName = Entry(self.root)
                self.inputFields.append(fieldName)
                self.inputFields[row].grid(row  = row, column = 1, sticky = "nsew", padx = 2, pady = 2)

            Button(self.root, text = "Enter", command = self.getInput).grid(row = 21, column = 1)

    def drawPriceResultScreen(self):
        pr = PriceResults()
        pr.priceResultMode = self.priceResultMode
        pr.userInput = self.userInput
        pr.priceStatistics = self.priceStatistics
        pr.run()

    def drawPriceGraphScreen(self):
        print("Loading graph...")
        p = PriceGraph(T.Tk())

        numYears = 3
        startYear = self.year - (numYears - 1)
        endYear = self.year + (numYears  - 1)
        if endYear > 2018:
            endYear = 2018
        p.setNumPoints(endYear - startYear + 1)

        for i in range(p.getNumPoints()):
            searchYear = startYear + i
            p.appendYear(searchYear)
            if startYear + i == self.year:
                amazonPrice, ebayPrice, walmartPrice = self.averagePrices
                p.appendPrice(0, amazonPrice)
                p.appendPrice(1, ebayPrice)
                p.appendPrice(2, walmartPrice)
            else:
                searchInput = self.userInput
                searchInput[1] = str(searchYear)
                priceStatistics, averagePrices = searchURLs(searchInput)
                amazonPrice, ebayPrice, walmartPrice = averagePrices
                p.appendPrice(0, amazonPrice)
                p.appendPrice(1, ebayPrice)
                p.appendPrice(2, walmartPrice)

        p.graphFromPoints()
        p.run()