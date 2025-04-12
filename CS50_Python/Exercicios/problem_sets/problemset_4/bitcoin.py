import sys
import requests

# Check for correct number of command-line arguments
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Try converting the argument to a float
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit(f"Command-line {sys.argv[1]} is not a number")

# Your CoinCap API key
API_KEY = "YourApiKey"  # Replace this with your actual API key

# Query CoinCap API
try:
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")
except (KeyError, TypeError, ValueError):
    sys.exit("Error parsing response")

# Calculate total cost
cost = n * price

# Output formatted price
print(f"${cost:,.4f}")
