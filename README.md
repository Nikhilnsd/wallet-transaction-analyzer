# 🔍 Ethereum Wallet Transaction Counter using Alchemy + Google Sheets

> Analyze Ethereum wallet activity by fetching transaction counts using [Alchemy](https://www.alchemy.com/) and dynamically updating a [Google Sheet](https://www.google.com/sheets/about/) with the results!

---

## 📌 Project Overview

This tool helps you:
✅ Fetch Ethereum wallet transaction counts
✅ Automate data syncing with Google Sheets
✅ Monitor multiple wallets with just one script

Perfect for analysts, researchers, DeFi teams, and anyone who needs scalable on-chain wallet data.

---

## 🚀 Features

* ⚡ Fetches real-time transaction counts using **Alchemy API**
* 🧾 Integrates with **Google Sheets API** via Service Account
* 🧠 Handles 100+ wallets with auto-throttling
* 📈 Outputs a clean, ready-to-analyze sheet
* 🛡️ Securely connects using OAuth2 credentials

---

## 🧉 Folder Structure

```
wallet-transaction-analyzer/
├── .env.example                  # Placeholder example (no real keys)
├── fetch_transactions.py        # Test single wallet
├── wallet_transaction_counter.py# Main script
├── README.md                    # Documentation
└── requirements.txt             # Python dependencies
                     # This documentation
```

---

## 🔧 Requirements

| Tool        | Version                          |
| ----------- | -------------------------------- |
| Python      | 3.8+                             |
| Alchemy API | Free/Pro Key                     |
| Google APIs | Enabled via Google Cloud Console |

Install dependencies:

```bash
pip install gspread oauth2client requests
```

---

## 🛠️ Setup Instructions

### 1. 🔑 Get an Alchemy API Key

* Go to [https://www.alchemy.com](https://www.alchemy.com)
* Create an account and a new Ethereum Mainnet app
* Copy the **HTTP API key** like:
  `https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY`

---

### 2. 📊 Prepare Google Sheet

1. Go to [Google Sheets](https://docs.google.com/spreadsheets)
2. Create a sheet with the structure:

```
| wallet_id                       |
|--------------------------------|
| 0x0039f22efb07a647...          |
| 0x06b51c6882b27cb0...          |
| ...                            |
```

> Only the **first row** (A1) should have the header `wallet_id`. Addresses go from A2 down.

---

### 3. 🔐 Google Service Account Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new **Service Account**
3. Enable **Google Sheets API** and **Google Drive API**
4. Download the `.json` key and place it in your project folder
5. Rename it (optional):
   `wallet-risk-analysis.json`
6. Share your Google Sheet with the service account email
   (e.g., `sheet-reader@project-id.iam.gserviceaccount.com`)
   → Set permission to **Editor**

---

## ⚙️ Configuration

Update the following values in `wallet_transaction_counter.py`:

```python
ALCHEMY_API_KEY = "your-alchemy-api-key"
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/your-sheet-id/edit#gid=0"
JSON_KEYFILE_NAME = "wallet-risk-analysis.json"
```

---

## ▶️ Run the Script

```bash
python wallet_transaction_counter.py
```

You’ll see output like:

```
🔍 Found 103 wallets.
1. Wallet: 0x0039...ef3 → Tx Count: 1817
2. Wallet: 0x06b5...988 → Tx Count: 3
...
✅ Transaction counts updated in Google Sheet.
```
📊 Results
You can view the final wallet transaction counts and intermediate results directly in this Google Sheet:

👉 [Click here to view the result spreadsheet](https://docs.google.com/spreadsheets/d/1i-eNRRGIfxg2ouTIMqCM1_24S2vyqrFTgR3Si7_NHO4/edit?gid=0#gid=0)


---


## 🧠 Why Use This?

✅ Scale wallet tracking across DeFi
✅ Automate risk or KYC workflows
✅ Compatible with DAOs, audits, and on-chain analytics

---

## 🙌 Acknowledgements

* [Alchemy](https://www.alchemy.com/)
* [Google Cloud](https://cloud.google.com/)
* [Gspread Library](https://gspread.readthedocs.io/)
* Ethereum ❤️

---

## 📄 License

MIT License — use freely, share proudly 🚀

---

> 💡 by Nikhil S Doshikar
