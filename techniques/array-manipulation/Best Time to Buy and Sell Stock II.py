def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit += price - min_price
            min_price = price
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices=prices))
# Output: 7

prices = [1, 2, 3, 4, 5]
print(maxProfit(prices=prices))
# Output: 4

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices=prices))
# Output: 0
