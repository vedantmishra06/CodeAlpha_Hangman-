import yfinance as yf

# In-memory portfolio
portfolio = {}

def add_stock(ticker, shares, purchase_price):
    if ticker in portfolio:
        portfolio[ticker]['shares'] += shares
        portfolio[ticker]['total_invested'] += shares * purchase_price
    else:
        portfolio[ticker] = {
            'shares': shares,
            'total_invested': shares * purchase_price
        }
    print(f"Added {shares} shares of {ticker} at ${purchase_price:.2f} each.")

def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from portfolio.")
    else:
        print(f"{ticker} not found in portfolio.")

def get_current_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'][-1]
    except:
        return None

def show_portfolio():
    print("\nYour Portfolio:")
    total_value = 0
    total_invested = 0

    for ticker, data in portfolio.items():
        current_price = get_current_price(ticker)
        if current_price is None:
            print(f"{ticker}: Unable to fetch data.")
            continue

        shares = data['shares']
        value = shares * current_price
        invested = data['total_invested']
        gain = value - invested
        percent = (gain / invested) * 100 if invested > 0 else 0

        print(f"{ticker}: {shares} shares | Current: ${current_price:.2f} | "
              f"Invested: ${invested:.2f} | Value: ${value:.2f} | Gain: ${gain:.2f} ({percent:.2f}%)")
        total_value += value
        total_invested += invested

    print(f"\nTotal Invested: ${total_invested:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")
    print(f"Total Gain/Loss: ${total_value - total_invested:.2f}\n")

def menu():
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
            shares = float(input("Enter number of shares: "))
            price = float(input("Enter purchase price per share: "))
            add_stock(ticker, shares, price)
        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            remove_stock(ticker)
        elif choice == '3':
            show_portfolio()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the tracker
menu()
