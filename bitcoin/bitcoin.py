import requests
import sys

try:
    nf = float(sys.argv[1])
except ValueError:
    sys.exit("Command-Line Argument is not a Number")
except IndexError:
    sys.exit("Missing Command-Line Argument")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0520e31e51867361078886b68b0d2bbb2a952dd9d5d5d6d79b4c1373de2dabc1")
    respsheet = response.json()
except requests.RequestException:
    sys.exit()

# idk how this works
for key, value in respsheet.items():
    if isinstance(value, dict):
        priceUsd = float(value["priceUsd"])

print(f"${(nf*priceUsd):,.4f}")
