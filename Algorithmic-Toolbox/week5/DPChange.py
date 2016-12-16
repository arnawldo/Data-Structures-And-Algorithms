# uses python3
''' find minimum number of coins to change certain amount of money
'''


changes = {}
def DPChange(money, coins):
    minNumCoins = {}
    minNumCoins[0] = 0
    for m in range(1, money + 1):
        minNumCoins[m] = float('inf')
        for coin in coins:
            if m >= coin:
                numCoins = minNumCoins[m - coin] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    return minNumCoins[money]

MONEY = 9
COINS = [1, 5, 6]

print(DPChange(MONEY, COINS))
