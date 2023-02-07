# solution1
def coinSolution(coin, target):
    """coin = [25, 10, 1]
    """
    for i in coin:
        print(i)
        if target >= i:
            (target // i) + coinSolution(target % i)   

ss = coinSolution(26)
print(ss)

# solution2 优化的暴力穷举(重复计算)
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#  solution3 消除solution2 的重复计算
def recMC(coinValueList, change, knowResults):
    """
    knowResults: 通过index来记录各个index的最优解 [0]*64
    """
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins
    return minCoins

# solution4 dynamic programming 
def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(1,change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        
        minCoins[cents] = coinCount #问题的最优解包含了更小规模子问题的最优解
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:   
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

change = 63
clist = [1,5,10,21,25]
coinUsed = [0] * (change + 1)
coinCount = [0] * (change + 1)
