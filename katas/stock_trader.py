def max_profit(prices):
    if not prices:
        return 0

    max_future_price = prices[-1]
    max_profit_result = 0

    for price in reversed(prices):
        max_profit_result = max(max_profit_result, max_future_price - price)
        max_future_price = max(max_future_price, price)

    return max_profit_result


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 5

    # Additional test cases
    prices1 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 0 (no profit possible)

    prices2 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 4 (buy at 1, sell at 5)
