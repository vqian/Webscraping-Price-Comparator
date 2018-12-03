from webscraping import *
from PriceGraph import *

p = PriceGraph(T.Tk())
p.setNumPoints(5)
for i in range(p.getNumPoints()):
    p.appendYear(1000 * i)
    p.appendPrice(100 * i)
p.graphFromPoints()
p.run()

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
