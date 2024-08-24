from requests import get

def scraper():
    url = 'https://production.api.coindesk.com/v2/tb/price/ticker?assets='

    symbol = input("Enter a Crypto symbol: ")

    data = get(url + symbol).json()

    try:
        coin_data = data["data"][symbol]
    except KeyError:
        print('ERROR: Enter a valid ISO symbol like "BTC"')
        return

    coin_prices = coin_data["ohlc"]
    coin_prices_c = round(coin_prices["c"], 2)

    print(f'Current Price for {coin_data["name"]} is {coin_prices_c}$')

if __name__ == "__main__":
    scraper()