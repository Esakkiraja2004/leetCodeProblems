prices = [2, 4, 1]
min_price = float('inf')
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print(max_profit)
