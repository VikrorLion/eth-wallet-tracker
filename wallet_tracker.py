import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")
API_URL = "https://api.etherscan.io/api"

def get_balance(address):
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": API_KEY
    }
    r = requests.get(API_URL, params=params)
    data = r.json()
    if data.get("status") == "1":
        eth = int(data["result"]) / 10**18
        return eth
    else:
        return None

if __name__ == "__main__":
    if API_KEY is None:
        print("Error: ETHERSCAN_API_KEY is not set. Create a .env file with ETHERSCAN_API_KEY=yourkey")
        exit(1)

    try:
        with open("wallets.txt") as f:
            addresses = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("wallets.txt not found. Create wallets.txt with one address per line.")
        exit(1)

    for addr in addresses:
        balance = get_balance(addr)
        if balance is not None:
            print(f"Address: {addr}\nBalance: {balance:.4f} ETH\n{'-'*28}")
        else:
            print(f"Address: {addr}\nError fetching balance.\n{'-'*28}")
