prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# zip() create an iterator that can only be consumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names))

# 按照key排序，输出结果也是key
print(min(prices))
print(max(prices))

# 按照value排序，输出结果也是value
print(min(prices.values()))
print(max(prices.values()))