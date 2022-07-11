class Coin():
    def __init__(self, coinType, index):
        self.type = coinType
        self.index = index

def makeChange(amount):
    types = {25, 10, 5, 1}
    map = []

def makeChange(amount, valueMap, coinType, index):
    if valueMap[amount].index > 0:
        return map[amount].index
    if index >= len(coinType):
        return 1
    coin = coinType[index]
    ways = 0
    i = 0
    while(amount > i * coin):
        amountLeft = amount - coin * i
        ways += makeChange(amountLeft, valueMap, coinType, index + 1)
        i+=1
    newValue = Coin(coin, ways)
    valueMap.append(newValue)
    return ways  
