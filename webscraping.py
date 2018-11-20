import requests

#url = "https://www.amazon.com/Dell-XPS-13-2018/s?page=1&rh=i%3Aaps%2Ck%3ADell%20XPS%2013%20%282018%29"
url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=Dell+XPS+15+(2018)&rh=i%3Aaps%2Ck%3ADell+XPS+15+(2018)"
website = requests.get(url)
source = website.text # HTML doc

from bs4 import BeautifulSoup

parser = BeautifulSoup(source, 'html.parser')
fullText = parser.get_text()

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
lowestPrice = prices[0]
highestPrice = prices[0]
sumPrices = 0
for price in prices:
    sumPrices += price
    lowestPrice = min(lowestPrice, price)
    highestPrice = max(highestPrice, price)
averagePrice = sumPrices / len(prices)
print("Lowest Price = $%0.2f" % lowestPrice)
print("Average Price = $%0.2f" % averagePrice)
print("Highest Price = $%0.2f" % highestPrice)