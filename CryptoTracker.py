import requests
import json
import time

API_URL = "https://api.coingecko.com/api/v3/simple/price"
CRYPTOCURRENCIES = ["bitcoin", "ethereum", "dogecoin"]

def fetch_prices(cryptos):
    """Fetch current prices for the given cryptocurrencies."""
    params = {
        'ids': ','.join(cryptos),
        'vs_currencies': 'usd'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def display_prices(prices):
    """Display the current prices of cryptocurrencies."""
    print("\nCryptocurrency Prices (in USD):")
    for crypto, data in prices.items():
        print(f"{crypto.capitalize()}: ${data['usd']}")

def save_prices_to_file(prices):
    """Save the current prices to a file."""
    filename = f"crypto_prices_{time.strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(prices, f, indent=4)
    print(f"Prices saved to {filename}")

def main():
    while True:
        print("\nCryptocurrency Price Tracker")
        print("1. Fetch and display current prices")
        print("2. Save current prices to file")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            prices = fetch_prices(CRYPTOCURRENCIES)
            if prices:
                display_prices(prices)
        elif choice == '2':
            prices = fetch_prices(CRYPTOCURRENCIES)
            if prices:
                save_prices_to_file(prices)
        elif choice == '3':
            print("Exiting the Cryptocurrency Price Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
