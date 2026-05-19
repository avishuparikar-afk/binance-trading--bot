# pyrefly: ignore [missing-import]
from binance.client import Client
# pyrefly: ignore [missing-import]
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logger import logger

def place_market_order(client: Client, symbol: str, side: str, quantity: float):
    """Place a MARKET order on Binance Futures Testnet."""
    try:
        logger.info(f"Placing MARKET {side} order for {quantity} {symbol}...")
        
        order_side = SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL
        
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=order_side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        
        logger.info(f"MARKET order successful! Order ID: {response.get('orderId')}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Failed to place MARKET order (API Error): {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Failed to place MARKET order (Request Error): {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during MARKET order: {e}")
        raise

def place_limit_order(client: Client, symbol: str, side: str, quantity: float, price: float):
    """Place a LIMIT order on Binance Futures Testnet."""
    try:
        logger.info(f"Placing LIMIT {side} order for {quantity} {symbol} at price {price}...")
        
        order_side = SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL
        
        response = client.futures_create_order(
            symbol=symbol.upper(),
            side=order_side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        
        logger.info(f"LIMIT order successful! Order ID: {response.get('orderId')}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Failed to place LIMIT order (API Error): {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Failed to place LIMIT order (Request Error): {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during LIMIT order: {e}")
        raise
