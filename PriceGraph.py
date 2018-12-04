"""
Referenced https://stackoverflow.com/questions/19888437/python-tkinter-graph,
https://stackoverflow.com/questions/44724111/tkinter-gui-graph
"""

import matplotlib.pyplot as mp
import tkinter as T, sys
import numpy as np

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

    def getProjection(self, years, prices0, prices1, prices2):
        projectedPrices0 = np.poly1d(np.polyfit(years, prices0, 1))(years)
        projectedPrices1 = np.poly1d(np.polyfit(years, prices1, 1))(years)
        projectedPrices2 = np.poly1d(np.polyfit(years, prices2, 1))(years)

        projectedPrices = []
        for year in range(len(years)):
            total = projectedPrices0[year] + projectedPrices1[year] + projectedPrices2[year]
            averageProjection = total / 3
            projectedPrices.append(averageProjection)
        
        lastPrice = projectedPrices[-1]
        depreciationFactor = (projectedPrices[-1] - projectedPrices[0]) / len(years)
        for year in range(years[-1], 2019):
            projectedPrice = lastPrice + depreciationFactor * (year - years[-1] + 1)
            projectedPrices.append(projectedPrice)

        tempDepreciation = int(depreciationFactor * 100)
        roundedDepreciationFactor = str(tempDepreciation // 100) + "." + str(tempDepreciation % 100)
        return projectedPrices, roundedDepreciationFactor

    def graphFromPoints(self):
        mp.ion()
        years = self.getYears()
        prices0, prices1, prices2 = self.getPrices()
        mp.plot(years, prices0)
        mp.plot(years, prices1)
        mp.plot(years, prices2)

        projectedPrices, depreciationFactor = self.getProjection(years, prices0, prices1, prices2)
        mp.plot(range(years[0], 2020), projectedPrices)

        mp.legend(("Amazon", "eBay", "Walmart", "Projected: Depreciation = $" + str(depreciationFactor) + " per year"))
        mp.title("Average Price over Time")
        mp.xlabel("Year")
        mp.ylabel("Price ($)")
        mp.draw()

    def run(self):
        self.root.mainloop()