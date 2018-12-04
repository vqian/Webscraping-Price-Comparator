from tkinter import *
from webscraping import *
from PriceComparator import *
import webbrowser
from LinkButton import *
from image_util import *

class PriceResults(object):
    def __init__(self):
        self.priceResultMode = True
        self.userInput = ""
        self.priceStatistics = ""
        self.images = []
        #self.run()

    def run(self, width = 600, height = 600):
        class Struct(object): pass
        self.width = width
        self.height = height
        #self.root = Tk()
        self.root = Toplevel()
        self.root.title("Price Comparator") # name of app
        self.root.resizable(width = False, height = False)

        self.drawPriceResultScreen()
        self.root.mainloop()

    def amazonHyperlink(self):
        webbrowser.open_new(self.amazonUrl)

    def ebayHyperlink(self):
        webbrowser.open_new(self.ebayUrl)

    def walmartHyperlink(self):
        webbrowser.open_new(self.walmartUrl)

    def drawPriceResultScreen(self):
        if self.priceResultMode:
            self.name = " ".join(self.userInput)
            print(self.name)
            print(self.priceStatistics)
            namePosition = self.height / 8

            self.canvas = Canvas(self.root, width = self.width, height = self.height)
            self.canvas.configure(bd = 0, highlightthickness = 0)
            self.canvas.pack()
            #self.canvas.delete("all")

            self.canvas.create_text(self.width / 2, namePosition, text = self.name, font = "Helvetica 20")
            pricesPosition = self.height * 3 // 5
            self.canvas.create_text(self.width / 2, pricesPosition, text = self.priceStatistics, font = "Helvetica 14")
               
            urls = getURLs(self.userInput)
            for i in range(len(urls)):
                """
                Code modified from http://code.activestate.com/recipes/580774-tkinter-link-or-hyperlink-button/
                """
                frame = Frame(self.root, bg = "white")
                frame.pack(expand = True, fill = "both")

                url = urls[i]
                if "amazon.com" in url:
                    self.amazonUrl = url
                    link = LinkButton(frame, text = "Hyperlink: " + self.amazonUrl, action = self.amazonHyperlink)
                    link.pack(padx = 10, pady = 10)
                elif "ebay.com" in url:
                    self.ebayUrl = url
                    link = LinkButton(frame, text = "Hyperlink: " + self.ebayUrl, action = self.ebayHyperlink)
                    link.pack(padx = 10, pady = 10)
                elif "walmart.com" in url:
                    self.walmartUrl = url
                    link = LinkButton(frame, text = "Hyperlink: " + self.walmartUrl, action = self.walmartHyperlink)
                    link.pack(padx = 10, pady = 10)
                """
                link = Label(self.root, text = "Hyperlink: " + urls[i], fg = "blue", cursor = "hand2")
                link.pack()
                link.bind("<Button-" + str(i + 1) + ">", lambda = self.hyperlink())
                """

            for image in self.images:
                print(image)
                linkImage = PhotoImageFromLink(image)
                self.canvas.create_image(self.width // 4, self.height // 2, anchor = NW, image = linkImage) 

"""
t = Tester()
t.run()
"""