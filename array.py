amazon_stocks = [3300, 2356, 3100, 3412, 3500]

day_one = amazon_stocks[0]
day_two = amazon_stocks[1]
day_three = amazon_stocks[2]
day_four = amazon_stocks[3]
day_five = amazon_stocks[4]

print(f"Amazon STOCK price on Day 1 is ${day_one}")
print(f"Amazon STOCK price on Day 4 is ${day_four}")

set_stock_price = {
    "January": 3300,
    "February": 2356,
    "March": 3100,
    "April": 3412,
    "May": 3500
}

for key, value in set_stock_price.items():
    print(key, "Stock Price is ", value)



