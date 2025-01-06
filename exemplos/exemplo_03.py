import requests

url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"
    }
params = {"currency": "USD"} #moeda consultada

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Preco do Bitcoin em USD: ", data["data"]["amount"])
