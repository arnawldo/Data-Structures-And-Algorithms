# uses python3
''' find minimum number of coins to change certain amount of money
'''

import sys

def recursiveChange(money, coins):
    if money == 0:
        return 0
    minNumCoins = float('inf')
    for coin in coins:
        if money >= coin:
            numCoins = recursiveChange(money - coin, coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins +1
    return minNumCoins

MONEY = 20
COINS = [1, 5, 6]

print(recursiveChange(MONEY, COINS))
