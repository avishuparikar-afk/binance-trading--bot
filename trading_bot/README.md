# Binance Futures Testnet Trading Bot

A professional, modular Python trading bot for placing MARKET and LIMIT orders on the Binance Futures Testnet.

## Project Overview

This project provides a robust framework for interacting with the Binance Futures API using the `python-binance` library. It includes:
- Clean modular architecture
- Interactive CLI for placing orders
- Input validation
- Robust error and exception handling
- Configurable logging system
- Environment variable management

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py        # Package initializer
│   ├── config.py          # Configuration and env var loading
│   ├── client.py          # Binance client initialization
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # User input validation
│   ├── logger.py          # Logging configuration
│   └── utils.py           # Helper functions
│
├── logs/                  # Log files directory (ignored by git)
├── screenshots/           # Directory for example screenshots
├── tests/                 # Unit tests directory
│
├── cli.py                 # Main CLI application
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables file
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- A Binance Futures Testnet Account

### 1. Installation

Clone the repository and navigate into the directory:
```bash
cd trading_bot
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Binance Testnet Setup

1. Go to [Binance Futures Testnet](https://testnet.binancefuture.com/)
2. Log in with your Binance account or create a testnet account.
3. Generate API Keys from the dashboard.
4. Note down both the `API Key` and the `API Secret`.

### 3. Environment Configuration

Copy the example environment file and update it with your keys:
```bash
cp .env.example .env
```
Edit `.env` and add your keys:
```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

### 4. How to Run

Execute the CLI application:
```bash
python cli.py
```

## Example Orders

### MARKET Order Example
```
=========================================
   BINANCE FUTURES TESTNET TRADING BOT   
=========================================
Type 'exit' or 'quit' at any prompt to cancel.

Enter symbol (e.g. BTCUSDT): BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity (e.g. 0.01): 0.1

Processing order...
2023-10-25 10:00:00 - INFO - TradingBot - Placing MARKET BUY order for 0.1 BTCUSDT...
2023-10-25 10:00:01 - INFO - TradingBot - MARKET order successful! Order ID: 123456789

========================================
ORDER RESPONSE SUMMARY
========================================
orderId             : 123456789
symbol              : BTCUSDT
status              : NEW
clientOrderId       : abcdefg
price               : 0
avgPrice            : 0.00000
origQty             : 0.1
executedQty         : 0
...
========================================
```

### LIMIT Order Example
```
Enter symbol (e.g. BTCUSDT): ETHUSDT
Enter side (BUY/SELL): SELL
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity (e.g. 0.01): 1.5
Enter price: 2000

Processing order...
2023-10-25 10:05:00 - INFO - TradingBot - Placing LIMIT SELL order for 1.5 ETHUSDT at price 2000.0...
2023-10-25 10:05:01 - INFO - TradingBot - LIMIT order successful! Order ID: 987654321

========================================
ORDER RESPONSE SUMMARY
========================================
orderId             : 987654321
symbol              : ETHUSDT
status              : NEW
...
========================================
```

## Logs

All operational logs and errors are automatically saved to `logs/trading_bot.log`. The logger handles both console output and rotating file backups to ensure the log file doesn't grow indefinitely.
