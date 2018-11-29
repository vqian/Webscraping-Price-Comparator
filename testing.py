from tkinter import *
#from UserInput import UserInput
from webscraping import *
from PriceComparator import *
import webbrowser
from Link_Button import *

class Tester(object):
    def __init__(self):
        self.priceResultMode = True
        self.userInput = ""
        self.priceStatistics = ""
        #self.run()

    def run(self, width = 600, height = 600):
        class Struct(object): pass
        self.width = width
        self.height = height
        self.root = Tk()
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
                    link = Link_Button(frame, text = "Hyperlink: " + self.amazonUrl, action = self.amazonHyperlink)
                    link.pack(padx = 10, pady = 10)
                elif "ebay.com" in url:
                    self.ebayUrl = url
                    link = Link_Button(frame, text = "Hyperlink: " + self.ebayUrl, action = self.ebayHyperlink)
                    link.pack(padx = 10, pady = 10)
                elif "walmart.com" in url:
                    self.walmartUrl = url
                    link = Link_Button(frame, text = "Hyperlink: " + self.walmartUrl, action = self.walmartHyperlink)
                    link.pack(padx = 10, pady = 10)
                """
                link = Label(self.root, text = "Hyperlink: " + urls[i], fg = "blue", cursor = "hand2")
                link.pack()
                link.bind("<Button-" + str(i + 1) + ">", lambda = self.hyperlink())
                """
"""
t = Tester()
t.run()
"""

"""
self.userInput = "Sample Product"
self.priceStatistics = "Sample Statistics"
p.drawPriceResultScreen()
"""

"""
def getUserInput(prompt):
    inputBox = UserInput(prompt)
    inputBox.waitForInput()
    return inputBox.getInput()

userInput = getUserInput("Please enter item name")
print("User Input:", userInput)
"""

################
# Testing code #
################

def testAmazon():
    url1 = "https://www.amazon.com/Dell-XPS-13-2018/s?page=1&rh=i%3Aaps%2Ck%3ADell%20XPS%2013%20%282018%29"
    url2 = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=Dell+XPS+15+(2018)&rh=i%3Aaps%2Ck%3ADell+XPS+15+(2018)"
    parseAmazon(url1)
    parseAmazon(url2)

def testEbay():
    url1 = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR2.TRC1.A0.H0.Xlava+lamp+14.5%22.TRS0&_nkw=lava+lamp+14.5%22&_sacat=0&LH_TitleDesc=0&_odkw=lava+lamp"
    url2 = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=lava+lamp+14.5%22+refurbished&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=lava+lamp+14.5%22&LH_TitleDesc=0"
    parseEbay(url1)
    parseEbay(url2)

def testWalmart():
    url1 = "https://www.walmart.com/search/?query=dell%20xps%2015%202018"
    url2 = "https://www.walmart.com/search/?query=dell%20xps%2015%202016&cat_id=0"
    parseWalmart(url1)
    parseWalmart(url2)

def testAll():
    print("Testing Amazon parsing...")
    testAmazon()
    print("Testing eBay parsing...")
    testEbay()
    print("Testing Walmart parsing...")
    testWalmart()
