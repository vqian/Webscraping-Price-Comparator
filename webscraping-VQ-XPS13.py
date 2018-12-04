##########################################################
# Back-end web-scraping with requests and Beautiful Soup #
##########################################################

import requests
from bs4 import BeautifulSoup

"""
Helper Method for searchURLs(userInput)
Parameters: list of strings userInput of keywords
Return: list of urls for Amazon, eBay, Walmart
"""
def getURLs(userInput):
    urls = []
    urlAmazon = "https://www.amazon.com/s?url=field-keywords="
    urlEbay = "https://ebay.com/sch/i.html?_nkw="
    urlWalmart = "https://www.walmart.com/search/?query="

    for keyword in userInput:
        keyword = keyword.replace(" ", "+")
        urlAmazon += keyword + "+"
        keyword = keyword.replace("+", "%20")
        urlEbay += keyword + "%20"
        urlWalmart += keyword + "%20"
    urlAmazon = urlAmazon[:-1]
    urlEbay = urlEbay[:-3]
    urlWalmart = urlWalmart[:-3]
    
    urls.append(urlAmazon)
    urls.append(urlEbay)
    urls.append(urlWalmart)
    
    return urls

"""
Parameters: list of strings userInput of keywords
Calls getURLs(userInput), parses prices on webpages of urls
"""
def searchURLs(userInput):
    result = ""
    averagePrices = []
    images = []

    urls = getURLs(userInput)
    for url in urls:
        if "amazon.com" in url:
            parsedResult, averagePrice, image = parseAmazon(url)
            result += parsedResult + "\n\n"
            averagePrices.append(averagePrice)
            images.append(image)
        elif "ebay.com" in url:
            parsedResult, averagePrice, image = parseEbay(url)
            result += parsedResult + "\n\n"
            averagePrices.append(averagePrice)
            images.append(image)
        elif "walmart.com" in url:
            parsedResult, averagePrice, image = parseWalmart(url)
            result += parsedResult + "\n\n"
            averagePrices.append(averagePrice)
            images.append(image)

    return result, averagePrices, images

"""
Parameters: string url
Return: string fullText of HTML file 
"""
def getHMTLText(url):
    website = requests.get(url)
    source = website.text # HTML doc
    """
    The following code uses saved HTML docs for testing when webscraping 
    cannot pass Recaptcha robot check
    """
    """
    source = ""
    if "amazon.com" in url:
        with open('AmazonHTML.txt', 'r') as file:
            source = file.read()
    elif "ebay.com" in url:
        with open('EbayHTML.txt', 'r') as file:
            source = file.read()
    elif "walmart.com" in url:
        with open('WalmartHTML.txt', 'r') as file:
            source = file.read()
    """

    parser = BeautifulSoup(source, 'html.parser')
    fullText = parser.get_text()

    return fullText

"""
Parameters: float array prices
Return: floats lowestPrice, averagePrice, highestPrice
"""
def calculatePriceStatistics(prices):
    lowestPrice, averagePrice, highestPrice = 0, 0, 0
    try:
        lowestPrice = prices[0]
        highestPrice = prices[0]
        sumPrices = 0
        for price in prices:
            sumPrices += price
            lowestPrice = min(lowestPrice, price)
            highestPrice = max(highestPrice, price)
        averagePrice = sumPrices / len(prices)
    except:
        print("Failed to parse:", prices)
        return lowestPrice, averagePrice, highestPrice

    return lowestPrice, averagePrice, highestPrice

"""
Parameters: floats lowestPrice, averagePrice, highestPrice
Prints formatted price statistics 
"""
def printPriceStatistics(lowestPrice, averagePrice, highestPrice):
    print("Lowest Price = $%0.2f" % lowestPrice)
    print("Average Price = $%0.2f" % averagePrice)
    print("Highest Price = $%0.2f" % highestPrice)

"""
Parameters: floats lowestPrice, averagePrice, highestPrice
Return: string of formatted price statistics 
"""
def formatPriceStatistics(lowestPrice, averagePrice, highestPrice):
    result = ""
    result += "Lowest Price = $%0.2f\n" % lowestPrice
    result += "Average Price = $%0.2f\n" % averagePrice
    result += "Highest Price = $%0.2f\n" % highestPrice
    return result

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
                try:
                    prices.append(float(price))
                except:
                    continue

    lowestPrice, averagePrice, highestPrice = calculatePriceStatistics(prices)

    image = parseImage(fullText)

    return ("Amazon Results:\n" + formatPriceStatistics(lowestPrice, averagePrice, highestPrice)), averagePrice, image

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

    image = parseImage(fullText)

    return ("eBay Results:\n" + formatPriceStatistics(lowestPrice, averagePrice, highestPrice)), averagePrice, image

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

    image = parseImage(fullText)

    return ("Walmart Results:\n" + formatPriceStatistics(lowestPrice, averagePrice, highestPrice)), averagePrice, image

def parseImage(fullText):
    """
    images = fullText.findAll('img', src = True)
    for image in images:
        print("Image: " + image)
    """

    #start = findNth(fullText, "img src=", 1)
    """
    start = fullText.find("data-image-src=")
    clippedText = fullText[start:]
    end = clippedText.find(".jpeg")
    """
    """
    jpg = clippedText.find(".jpeg")
    png = clippedText.find(".png")
    end = min(jpg, png)
    if jpg == -1:
        end = png
    elif png == -1:
        end = jpg
    """
    #clippedText = clippedText[15:end + 5]

    images = fullText.findAll("a", {"class":"image"})
    for image in images:
        print(image.img['src'])

    return clippedText

"""
Code modified from https://www.tutorialspoint.com/How-to-find-the-nth-occurrence-of-substring-in-a-string-in-Python
"""
def findNth(string, substring, n):
    substrings = string.split(substring, n + 1)
    if len(substrings) <= n + 1:
        return -1
    return len(string) - len(substrings[-1]) - len(substring)