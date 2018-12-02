"""
Code adapted from https://stackoverflow.com/questions/19888437/python-tkinter-graph
Also referenced https://stackoverflow.com/questions/44724111/tkinter-gui-graph
"""

import matplotlib.pyplot as mp
import tkinter as T, sys

class Application():

    """
    Beginning of own code
    """
    def __init__(self, root):
        self.root = root 

        self.x1 = []
        self.y2 = []
        self.z = 0

        self.root.title("GRAPH")
        self.root.geometry("600x600")
        self.root.config(bg = "light gray")
    """
    End of own code
    """

    def __init__(self, root):

        self.root = root

        self.x1 = []
        self.y2 = []

        self.z = 0

        self.root.title("GRAPH")
        self.root.geometry("600x600")
        self.root.config(bg = "light gray")

        self.e = T.Entry(self.root, justify = "center")

        self.l = T.Label(self.root, text = "Please enter number of coordinates: ", bg = "gray")

        self.b1 = T.Button(self.root, text = "OK", command = self.check)

        self.b2 = T.Button(self.root, text = "Graph", command = self.graph)
        self.b = T.Button(self.root, text = "Exit", command = self.end)

        self.l.pack()
        self.e.pack()
        self.b1.pack()

        self.b2.pack()
        self.b.pack()

    def run(self):
        self.root.mainloop()

    def end(self):
        sys.exit()

    def check(self):
        try:
            self.entry_x = []
            self.entry_y = []

            self.z = int(self.e.get())

            self.e.config(bg = "green")
            self.e.after(1000, lambda: self.e.config(bg = "white"))

            self.l2 = T.Label(self.root, text = "X", bg = "yellow")
            self.l2.pack()

            for i in range(self.z):
                self.entry_x.append(T.Entry(self.root, justify = "center"))
                self.entry_x[-1].pack()

            self.l3 = T.Label(self.root, text = 'Y', bg = '#3366ff')
            self.l3.pack()

            for i in range(self.z):
                self.entry_y.append(T.Entry(self.root, justify = "center"))
                self.entry_y[-1].pack() 
        except:
            self.e.config(bg = 'red')
            self.e.after(1000, lambda: self.e.config(bg = "white"))

    """
    Beginning of own code
    """
    def getNumPoints(self):
        return self.z

    def setNumPoints(self, numPoints):
        self.z = numPoints

    def appendToX(self, n):
        self.x1.append(n)

    def appendToY(self, n):
        self.y1.append(n)

    def graphFromPoints(self):
        years = self.x1
        prices = self.y1

        mp.ion()
        mp.plot(years, prices)  
        mp.title("Price Analysis")
        mp.xlabel("Year")
        mp.ylabel("Price ($)")
        mp.draw()
    """
    End of own code
    """

    def graph(self):
        self.x1 = []
        self.y1 = []

        for i in range(len(self.entry_x)):
            self.x1.append(float(self.entry_x[i].get()))

        for i in range(len(self.entry_y)):
            self.y1.append(float(self.entry_y[i].get()))

        mp.ion()
        mp.plot(self.x1, self.y1)  
        mp.title("Price Analysis")
        mp.xlabel("Year")
        mp.ylabel("Price ($)")
        mp.draw()

"""
Run Program
"""
#Application(T.Tk()).run()