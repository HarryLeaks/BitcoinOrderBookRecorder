import ccxt
import matplotlib.pyplot as plt
import time

# Create a Binance exchange object
exchange = ccxt.binance()

# Set the symbol for the order book
symbol = 'BTC/USDT'
fig = plt.figure()
ax = fig.add_subplot()

while True:
    # Fetch the order book data
    order_book = exchange.fetch_l2_order_book(symbol)

    # Get the bid and ask prices and quantities
    bids_prices, bids_quantities = zip(*order_book['bids'])
    asks_prices, asks_quantities = zip(*order_book['asks'])

    # Create a cumulative sum of bid and ask quantities
    cumulative_bids = [sum(bids_quantities[:i + 1]) for i in range(len(bids_quantities))]
    cumulative_asks = [sum(asks_quantities[:i + 1]) for i in range(len(asks_quantities))]

    # Clear the axis before re-plotting
    ax.clear()

    # Plot the DOM graph with bars
    ax.bar(bids_prices, cumulative_bids, color='g', alpha=0.7, align='edge', width=-0.5, label='Bids')
    ax.bar(asks_prices, cumulative_asks, color='r', alpha=0.7, align='edge', width=0.5, label='Asks')

    # Set the title and labels
    ax.set_title('Depth of Market (DOM) - Bids and Asks')
    ax.set_xlabel('Price')
    ax.set_ylabel('Cumulative Quantity')

    # Add a legend
    ax.legend()

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show(block=False)
    plt.pause(1)
