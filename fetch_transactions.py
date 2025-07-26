import requests
import json
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("ALCHEMY_API_KEY")
ALCHEMY_URL = f"https://eth-mainnet.g.alchemy.com/v2/{API_KEY}"

wallet_address = "0x0039f22efb07a647557c7c5d17854cfd6d489ef3"

def get_transaction_count(wallet):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionCount",
        "params": [wallet, "latest"],
        "id": 1
    }

    response = requests.post(ALCHEMY_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    data = response.json()

    if "result" in data:
        tx_count = int(data["result"], 16)
        print(f"Wallet: {wallet} → Transaction Count: {tx_count}")
    else:
        print("Error in response:", data)

get_transaction_count(wallet_address)
