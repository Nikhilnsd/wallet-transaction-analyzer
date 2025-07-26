import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import requests
import time

# Load environment variables from .env
load_dotenv()

# --- Configuration ---
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
ALCHEMY_URL = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(GOOGLE_SHEET_URL)
worksheet = sheet.sheet1

# --- Read Wallet IDs from Column A (skip header) ---
wallets = worksheet.col_values(1)[1:]
wallets = [w for w in wallets if w.startswith("0x") and len(w) == 42]

print(f"🔍 Found {len(wallets)} wallets.")

# --- Fetch Transaction Count for Each Wallet ---
results = []
for i, wallet in enumerate(wallets):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionCount",
        "params": [wallet, "latest"],
        "id": 1
    }
    try:
        response = requests.post(ALCHEMY_URL, json=payload)
        tx_count = int(response.json()["result"], 16)
        results.append([tx_count])
        print(f"{i+1}. Wallet: {wallet} → Tx Count: {tx_count}")
    except Exception as e:
        results.append(["Error"])
        print(f"{i+1}. Wallet: {wallet} → ❌ Error: {e}")
    time.sleep(0.2)

# --- Update Google Sheet in Column B ---
worksheet.update("B1", [["transaction_count"]] + results)
print("✅ Transaction counts updated in Google Sheet.")
