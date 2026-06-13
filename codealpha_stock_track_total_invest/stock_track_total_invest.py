# ----- Stock Portfolio Tracker -----
# Author: Ujjawal
# Internship Task 2 - CodeAlpha

def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320,
        "GOOG": 140,
        "AMZN": 130
    }

    print("---- Welcome to Stock Portfolio Tracker ----")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    total_investment = 0
    portfolio = {}

    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol! Please choose from available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment
        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"Added {quantity} shares of {stock} worth ${investment}")

    print("\n---- Portfolio Summary ----")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares (Price: ${stock_prices[stock]} each)")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optionally save to file
    save_choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save_choice == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("---- Portfolio Summary ----\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares (Price: ${stock_prices[stock]} each)\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Portfolio saved to portfolio.txt")

# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()
