coin_denomination = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(change):
    
    result = {}
    for coin in coin_denomination:
        if change >= coin:
            count = change // coin
            result[coin] = count
            change -= coin * count
    return result


def find_min_coins(amount):    
    dp = [0] + [float("inf")] * amount
    track = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coin_denomination:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                track[i] = coin

    result = {}
    while amount > 0:
        coin = track[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result


# Tests
print("Greedy 747:", find_coins_greedy(747))
print("Dynamic 747:", find_min_coins(747))
