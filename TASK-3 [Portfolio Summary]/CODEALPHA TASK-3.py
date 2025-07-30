stock_prices = {
    "SENSEX": 180,
    "TSLA": 250,
    "NIFTY": 310,
    "BNB": 140,
    "MSFT": 130
}
portfolio = {}
total_investment = 0
# Get number of stocks from user
num_stocks = int(input("Enter the number of stocks you want to add: "))
for _ in range(num_stocks):
    stock = input("Enter stock name (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        portfolio[stock] = {
            "price": stock_prices[stock],
            "quantity": quantity,
            "investment": investment
        }
        total_investment += investment
    else:
        print(f"Stock '{stock}' not found in the price list.")
# Display results
print("\nPortfolio Summary:")
for stock, info in portfolio.items():
    print(f"{stock}: {info['quantity']} shares x ${info['price']} = ${info['investment']}")
print(f"\nTotal Investment Value: ${total_investment}")
# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, info in portfolio.items():
            file.write(f"{stock}: {info['quantity']} shares x ${info['price']} = ${info['investment']}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("Portfolio saved to 'portfolio_summary.txt'")
