def filter_prices(prices):
    filtered_prices = {}
    for key, value in prices.items():
        if value > 200:
            filtered_prices[key] = value
    return filtered_prices


prices = {
    'ACME': 43.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

filtered_prices = filter_prices(prices)
print(filtered_prices)
