from coinbase.wallet.client import Client
client = Client( < api_key > , < api_secret > )

accounts = client.get_accounts()
