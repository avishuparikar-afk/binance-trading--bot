import re

def validate_symbol(symbol: str) -> bool:
    """Validate trading symbol format (e.g., BTCUSDT)."""
    return bool(re.match(r'^[A-Z0-9-]{3,15}$', symbol))

def validate_side(side: str) -> bool:
    """Validate order side (BUY or SELL)."""
    return side.upper() in ['BUY', 'SELL']

def validate_order_type(order_type: str) -> bool:
    """Validate order type (MARKET or LIMIT)."""
    return order_type.upper() in ['MARKET', 'LIMIT']

def validate_quantity(quantity: float) -> bool:
    """Validate that quantity is greater than 0."""
    return quantity > 0

def validate_price(price: float) -> bool:
    """Validate that price is greater than 0."""
    return price > 0

def validate_order_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> list:
    """Validate all order inputs. Returns a list of error messages, empty if valid."""
    errors = []
    if not validate_symbol(symbol):
        errors.append(f"Invalid symbol: {symbol}")
    if not validate_side(side):
        errors.append(f"Invalid side: {side}. Must be BUY or SELL.")
    if not validate_order_type(order_type):
        errors.append(f"Invalid order type: {order_type}. Must be MARKET or LIMIT.")
    if not validate_quantity(quantity):
        errors.append(f"Invalid quantity: {quantity}. Must be > 0.")
    if order_type.upper() == 'LIMIT' and (price is None or not validate_price(price)):
        errors.append("Price is required and must be > 0 for LIMIT orders.")
        
    return errors
