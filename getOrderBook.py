import ccxt
import csv
import datetime

# Create a Binance exchange object
exchange = ccxt.binance()

# Set the symbol and timeframe for the order book
symbol = 'BTC/USDT'

# Open a CSV file for writing
csv_file = open("order_book.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Date", "Symbol", "Price", "Quantity", "Side"])

try:
    while True:
        # Fetch the order book data
        order_book = exchange.fetch_l2_order_book(symbol)

        # Process and save the order book data to CSV
        timestamp = exchange.milliseconds()
        date = datetime.datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
        for bid in order_book['bids']:
            price, quantity = bid
            csv_writer.writerow([date, symbol, price, quantity, "Bid"])
        for ask in order_book['asks']:
            price, quantity = ask
            csv_writer.writerow([date, symbol, price, quantity, "Ask"])

        csv_file.flush()

except KeyboardInterrupt:
    pass

# Close the CSV file
csv_file.close()
