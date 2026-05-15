import requests
import time
from rich.console import Console
from rich.table import Table

# Currency and metal lists
currencies = ['usd', 'eur', 'sar']
metals = ['gold', 'silver']

# API URLs
currency_url = 'https://api.coingecko.com/api/v3/simple/price'
metal_url = 'https://metals-api.com/api/latest?access_key=YOUR_API_KEY&base=USD'

# USD to PKR conversion rate
usd_to_pkr = 282.50

# Rich console object
console = Console()

while True:
    try:
        # Request currency data from CoinGecko
        response = requests.get(
            currency_url,
            params={
                'ids': 'tether',
                'vs_currencies': ','.join(currencies)
            }
        )

        currency_data = response.json()

        # Sample metal data
        # Replace with real API response if API key is available
        metal_data = {
            "gold": 62.35,
            "silver": 0.80
        }

        # Clear screen
        console.clear()

        # Create table
        table = Table(title="Live Currency & Precious Metal Prices (PKR)")

        table.add_column("Commodity", justify="center", style="cyan", no_wrap=True)
        table.add_column("Price (PKR)", justify="center", style="green")

        # Currency names
        currency_names = {
            "usd": "Dollar (USD)",
            "eur": "Euro (EUR)",
            "sar": "Saudi Riyal (SAR)"
        }

        # Add currency prices
        for currency in currencies:
            price = f"₨{currency_data['tether'][currency] * usd_to_pkr:,.2f}"
            table.add_row(currency_names[currency], price)

        # Add metal prices
        for metal in metals:
            price = f"₨{metal_data[metal] * usd_to_pkr:,.2f}"
            table.add_row(metal.capitalize() + " (per gram)", price)

        # Print table
        console.print(table)

        # Refresh every 5 seconds
        time.sleep(5)

    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")
        break

    except Exception as e:
        print(f"Error: {e}")
        break