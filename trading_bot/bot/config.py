import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Binance API Keys
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")

# Binance Futures Testnet URL
TESTNET_URL = "https://testnet.binancefuture.com"
