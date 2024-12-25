def maxProfit(prices: list):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices=prices))
# Output: 5

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices=prices))
# Output: 0
