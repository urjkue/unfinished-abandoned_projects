import ccxt
import matplotlib.pyplot as plt
import datetime

def plot_price_chart(symbol, timeframe='1d'):
    exchange = ccxt.binance()  # Change this to your preferred exchange
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe)

    timestamps = [datetime.datetime.fromtimestamp(ts[0] / 1000) for ts in ohlcv]
    closing_prices = [price[4] for price in ohlcv]

    plt.plot(timestamps, closing_prices)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{symbol} Price Chart ({timeframe})')
    plt.xticks(rotation=45)
    plt.show()

def connect_to_exchange(api_key, secret_key):
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': secret_key,
    })

    # Print account balances
    balances = exchange.fetch_balance()
    print("Account Balances:")
    for currency, balance in balances['total'].items():
        print(f"{currency}: {balance}")

    return exchange

if __name__ == '__main__':
    # Example usage
    symbol = 'BTC/USDT'
    timeframe = '1d'
    plot_price_chart(symbol, timeframe)

    # Example connecting to an exchange
    api_key = 'your_api_key'
    secret_key = 'your_secret_key'
    exchange = connect_to_exchange(api_key, secret_key)
