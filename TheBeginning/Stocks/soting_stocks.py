stocks = {
    'GOOG': 500,
    'APPL': 100,
    'YHOO': 39,
    'AMZN': 40
}

print("Minimum: ")
print(min(zip(stocks.values(), stocks.keys())))

print("Maximum: ")
print(max(zip(stocks.values(), stocks.keys())))

print("\nSorted: ")
print(sorted(zip(stocks.values(), stocks.keys())))

