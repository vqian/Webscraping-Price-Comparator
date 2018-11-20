##########################################################
# Back-end web-scraping with requests and Beautiful Soup #
##########################################################

import requests

"""
Parameters: string url
Return: string fullText of HTML file 
"""
def getHMTLText(url):
    website = requests.get(url)
    source = website.text # HTML doc

    from bs4 import BeautifulSoup

    parser = BeautifulSoup(source, 'html.parser')
    fullText = parser.get_text()

    return fullText

"""
Parameters: float array prices
Return: floats lowestPrice, averagePrice, highestPrice
"""
def calculatePriceStatistics(prices):
    lowestPrice = prices[0]
    highestPrice = prices[0]
    sumPrices = 0
    for price in prices:
        sumPrices += price
        lowestPrice = min(lowestPrice, price)
        highestPrice = max(highestPrice, price)
    averagePrice = sumPrices / len(prices)

    return lowestPrice, averagePrice, highestPrice

"""
Parameters: floats lowestPrice, averagePrice, highestPrice
Prints formatted price statistics 
"""
def printPriceStatistics(lowestPrice, averagePrice, highestPrice):
    print("Lowest Price = $%0.2f" % lowestPrice)
    print("Average Price = $%0.2f" % averagePrice)
    print("Highest Price = $%0.2f" % highestPrice)

#############################
# Parsing prices for Amazon #
#############################

def parseAmazon(url):
    fullText = getHMTLText(url)

    start = fullText.find("Showing selected results")
    end =  fullText.find("Previous Page")
    clippedText = fullText[start : end]

    prices = []
    count = 0
    for fragment in clippedText.split("$"):
        count += 1
        if count % 2 == 0:
            price = fragment.splitlines()[0]
            if len(price) <= 10 and len(price) >= 3:
                price = price.replace(",", "")
                prices.append(float(price))

    lowestPrice, averagePrice, highestPrice = calculatePriceStatistics(prices)

    printPriceStatistics(lowestPrice, averagePrice, highestPrice)

###########################
# Parsing prices for eBay #
###########################

import re

def parseEbay(url):
    fullText = getHMTLText(url)

    start = fullText.find("results")
    end = fullText.find("Page")
    clippedText = fullText[start : end]

    prices = []
    for fragment in clippedText.split("$"):
            fragment = fragment.lower()
            fragment = re.split('[a-z]+', fragment)[0]
            price = fragment

            try:
                prices.append(float(price))
            except:
                pass

    lowestPrice, averagePrice, highestPrice = calculatePriceStatistics(prices)

    printPriceStatistics(lowestPrice, averagePrice, highestPrice)

##############################
# Parsing prices for Walmart #
##############################

def parseWalmart(url):
    fullText = getHMTLText(url)

    start = fullText.find("Current Price")
    end = fullText.find("Next Page")
    clippedText = fullText[start : end]

    prices = []
    for fragment in clippedText.split("$"):
            fragment = fragment.lower()
            fragment = re.split('[a-z]+', fragment)[0]
            price = fragment

            try:
                prices.append(float(price))
            except:
                pass

    lowestPrice, averagePrice, highestPrice = calculatePriceStatistics(prices)

    printPriceStatistics(lowestPrice, averagePrice, highestPrice)