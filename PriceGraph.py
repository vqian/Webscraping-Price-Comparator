"""
Referenced https://stackoverflow.com/questions/19888437/python-tkinter-graph,
https://stackoverflow.com/questions/44724111/tkinter-gui-graph
"""

import matplotlib.pyplot as mp
import tkinter as T, sys

class PriceGraph():
    def __init__(self, root):
        self.root = root 

        self.years = []
        self.prices0 = []
        self.prices1 = []
        self.prices2 = []
        self.numPoints = 0

    def getNumPoints(self):
        return self.numPoints

    def setNumPoints(self, numPoints):
        self.numPoints = numPoints

    def getYears(self):
        return self.years

    def getPrices(self):
        return self.prices0, self.prices1, self.prices2

    def appendYear(self, n):
        self.years.append(n)

    def appendPrice(self, index, n):
        if index == 0:
            self.prices0.append(n)
        elif index == 1:
            self.prices1.append(n)
        else:
            self.prices2.append(n)

    def graphFromPoints(self):
        mp.ion()
        years = self.getYears()
        prices0, prices1, prices2 = self.getPrices()
        mp.plot(years, prices0)
        mp.plot(years, prices1)
        mp.plot(years, prices2)
        mp.legend(("Amazon", "eBay", "Walmart"))
        mp.title("Average Price over Time")
        mp.xlabel("Year")
        mp.ylabel("Price ($)")
        mp.draw()

    def run(self):
        self.root.mainloop()