class CachedResults(object):
    def __init__(self):
        self.allResults = dict()

    def cacheResults(self, userInput, priceStatistics, averagePrices):
        self.allResults[userInput] = (priceStatistics, averagePrices)

    def isCached(self, userInput):
        return userInput in self.allResults

    def getAllCachedResults(self):
        return self.allResults

    def getCachedPriceStatistics(self, userInput):
        if not isCached(userInput):
            return None
        return self.allResults.get(userInput)