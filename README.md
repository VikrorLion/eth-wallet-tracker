# 🪙 ETH Wallet Tracker

Track Ethereum wallet balances in real-time using a simple Python script and public blockchain APIs.

---

## 💡 Features

- Reads wallet addresses from a text file
- Fetches ETH balance for each address via Etherscan API
- Supports testnets and mainnet
- Lightweight and easy to customize

---

## ⚙️ Setup

### 1. Clone repository

    git clone https://github.com/yourusername/eth-wallet-tracker.git
    cd eth-wallet-tracker

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Add your Etherscan API key  
Get a free key here: https://etherscan.io/apis

Create a `.env` file (or set environment variable):

    ETHERSCAN_API_KEY=yourapikey

---

## ▶️ Usage

    python wallet_tracker.py

---

## 🧾 Example output

    Address: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
    Balance: 2341.1293 ETH
    ----------------------------
    Address: 0x281055afc982d96fab65b3a49cac8b878184cb16
    Balance: 102.4321 ETH

---

## 📁 File structure

    eth-wallet-tracker/
    ├── wallet_tracker.py
    ├── wallets.txt
    ├── requirements.txt
    └── README.md

---

## 🌍 RU Version

Отслеживай балансы Ethereum-кошельков с помощью простого скрипта на Python.

### 🔹 Возможности
- Читает список адресов из файла
- Получает баланс через API Etherscan
- Работает с тестовой и основной сетью
- Легко модифицируется

---

## 🧠 Author

Created by [Viktor Leonenko](https://github.com/VikrorLion)  
Web3 enthusiast 💎 | Python + Blockchain integration
