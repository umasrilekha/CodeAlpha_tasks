# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue
    
    qty = int(input("Enter quantity: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value

print("\n===== SUMMARY =====")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares | ₹{qty * stock_prices[stock]}")

print("\nTOTAL INVESTMENT:", total_value)

with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Investment: {total_value}\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares\n")

print("\nReport saved to portfolio_report.txt")
