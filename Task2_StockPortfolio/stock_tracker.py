# Task 2 - Stock Portfolio Tracker
# Concepts used: dictionary, input/output, basic arithmetic,
#                file handling, csv module, OOP (class, object)

import csv

# ----------------------------------------
# CLASS - StockPortfolio
# Groups all portfolio data and operations
# into one class using OOP
# ----------------------------------------
class StockPortfolio:

    # __init__ sets up the stock prices dictionary and an empty portfolio list
    def __init__(self):
        # Hardcoded stock prices in a dictionary
        self.stock_prices = {
            "AAPL":  180,
            "TSLA":  250,
            "GOOGL": 140,
            "AMZN":  175,
            "MSFT":  320
        }
        self.portfolio = []      # list to store added stocks
        self.total = 0           # total investment amount

    # Method to show all available stocks
    def show_stocks(self):
        print("\nAvailable stocks and prices:")
        for stock in self.stock_prices:
            print(stock, "-", self.stock_prices[stock], "USD")

    # Method to add a stock to the portfolio
    def add_stock(self, stock_name, quantity):

        # Check if stock exists in dictionary
        if stock_name not in self.stock_prices:
            print("Stock not found. Please choose from the list above.")
            return

        price = self.stock_prices[stock_name]
        value = price * quantity

        # Store as a dictionary inside the list
        entry = {
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "value": value
        }
        self.portfolio.append(entry)
        self.total = self.total + value
        print("Added:", stock_name, "x", quantity, "=", value, "USD")

    # Method to display the final portfolio summary
    def show_summary(self):
        print("\n--- Portfolio Summary ---")
        for entry in self.portfolio:
            print(entry["stock"], "x", entry["quantity"], "=", entry["value"], "USD")
        print("Total Investment:", self.total, "USD")

    # Method to save results to a CSV file using csv module
    def save_to_csv(self):
        file = open("portfolio_result.csv", "w", newline="")
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Stock", "Quantity", "Price (USD)", "Total Value (USD)"])

        # Write each stock row
        for entry in self.portfolio:
            writer.writerow([entry["stock"], entry["quantity"], entry["price"], entry["value"]])

        # Write the total at the bottom
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", self.total])

        file.close()
        print("Portfolio saved to portfolio_result.csv")

    # Method to also save a plain text backup file
    def save_to_txt(self):
        file = open("portfolio_result.txt", "w")
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")
        for entry in self.portfolio:
            line = entry["stock"] + " x " + str(entry["quantity"]) + " = " + str(entry["value"]) + " USD"
            file.write(line + "\n")
        file.write("Total Investment: " + str(self.total) + " USD\n")
        file.close()
        print("Portfolio also saved to portfolio_result.txt")


# ----------------------------------------
# Create an object and run the tracker
# ----------------------------------------
tracker = StockPortfolio()   # create object from the class

print("Welcome to Stock Portfolio Tracker!")
tracker.show_stocks()

print("\nEnter your stocks below.")
print("Type 'done' when finished.\n")

# Keep asking until user types done
while True:
    stock_name = input("Enter stock name (e.g. AAPL): ").upper()

    if stock_name == "DONE":
        break

    quantity = int(input("Enter quantity: "))
    tracker.add_stock(stock_name, quantity)

# Show summary and save files
tracker.show_summary()
tracker.save_to_csv()
tracker.save_to_txt()
