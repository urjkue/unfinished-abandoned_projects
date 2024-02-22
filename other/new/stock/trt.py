# import random

# class Stock:
#     def __init__(self, symbol, price):
#         self.symbol = symbol
#         self.price = price
#         self.quantity = 0  # Initialize quantity to 0

#     def __str__(self):
#         return f"{self.symbol}: ${self.price:.2f} (Quantity: {self.quantity})"

# class StockMarket:
#     def __init__(self):
#         self.stocks = {}
#         self.balance = 10000  # Starting balance for each user

#     def add_stock(self, stock):
#         self.stocks[stock.symbol] = stock

#     def update_prices(self):
#         for stock in self.stocks.values():
#             # Simulating price changes with a random percentage change
#             percent_change = random.uniform(-5, 5)  # -5% to +5%
#             stock.price *= (1 + percent_change / 100)

#     def buy_stock(self, symbol, quantity):
#         if symbol not in self.stocks:
#             return "Stock not found."

#         stock = self.stocks[symbol]
#         total_cost = stock.price * quantity

#         if total_cost <= self.balance:
#             stock.quantity += quantity  # Update the quantity owned by the user
#             self.balance -= total_cost
#             return f"Bought {quantity} shares of {stock.symbol} for ${total_cost:.2f}."
#         else:
#             return "Insufficient balance to buy the stock."

#     def sell_stock(self, symbol, quantity):
#         if symbol not in self.stocks:
#             return "Stock not found."

#         stock = self.stocks[symbol]
#         if quantity <= 0 or quantity > stock.quantity:
#             return "Invalid quantity to sell."

#         total_price = stock.price * quantity
#         stock.quantity -= quantity  # Update the quantity owned by the user
#         self.balance += total_price
#         return f"Sold {quantity} shares of {stock.symbol} for ${total_price:.2f}."

#     def display_portfolio(self):
#         print("\nYour Portfolio:")
#         print(f"Balance: ${self.balance:.2f}")
#         for stock in self.stocks.values():
#             print(stock)

# # Creating the stock market and adding some initial stocks
# market = StockMarket()
# stock1 = Stock("AAPL", 150.0)
# stock2 = Stock("GOOG", 2500.0)
# stock3 = Stock("AMZN", 3500.0)
# market.add_stock(stock1)
# market.add_stock(stock2)
# market.add_stock(stock3)

# # Simulate trading for a few days
# for day in range(1, 6):
#     print(f"\n----- Day {day} -----")
#     market.update_prices()
#     market.display_portfolio()

#     # Simulate buying and selling (you can modify these as needed)
#     stock_to_buy = random.choice(list(market.stocks.keys()))
#     stock_to_sell = random.choice(list(market.stocks.keys()))
#     quantity_to_buy = random.randint(1, 10)
#     quantity_to_sell = random.randint(1, 10)

#     print(market.buy_stock(stock_to_buy, quantity_to_buy))
#     print(market.sell_stock(stock_to_sell, quantity_to_sell))

# print("\nFinal Portfolio:")
# market.display_portfolio()
