# pyrefly: ignore [missing-import]
from binance.client import Client
from bot.config import BINANCE_API_KEY, BINANCE_API_SECRET
from bot.logger import logger
# pyrefly: ignore [missing-import]
from binance.exceptions import BinanceAPIException, BinanceRequestException

def get_binance_client() -> Client:
    """Create and return a Binance client connected to Futures Testnet."""
    try:
        if not BINANCE_API_KEY or not BINANCE_API_SECRET:
            logger.error("API Keys are missing. Please check your .env file.")
            raise ValueError("Missing API keys.")
            
        logger.info("Initializing Binance Futures Testnet client...")
        
        # testnet=True configures the client to connect to Binance Testnet
        client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)
        
        # Check connection by fetching exchange info for futures
        client.futures_exchange_info()
        logger.info("Successfully connected to Binance Futures Testnet.")
        
        return client
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Binance Request Exception: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while creating client: {e}")
        raise
