import sys
from bot.client import get_binance_client
from bot.validators import validate_order_inputs
from bot.orders import place_market_order, place_limit_order
from bot.utils import print_order_response
from bot.logger import logger

def main():
    print("=========================================")
    print("   BINANCE FUTURES TESTNET TRADING BOT   ")
    print("=========================================")
    print("Type 'exit' or 'quit' at any prompt to cancel.\n")
    
    try:
        # Initialize client
        client = get_binance_client()
        
        while True:
            try:
                # Get inputs
                symbol = input("Enter symbol (e.g. BTCUSDT): ").strip().upper()
                if symbol.lower() in ['exit', 'quit']: break
                
                side = input("Enter side (BUY/SELL): ").strip().upper()
                if side.lower() in ['exit', 'quit']: break
                
                order_type = input("Enter order type (MARKET/LIMIT): ").strip().upper()
                if order_type.lower() in ['exit', 'quit']: break
                
                quantity_str = input("Enter quantity (e.g. 0.01): ").strip()
                if quantity_str.lower() in ['exit', 'quit']: break
                try:
                    quantity = float(quantity_str)
                except ValueError:
                    print("Invalid quantity! Must be a number.\n")
                    continue
                
                price = None
                if order_type == 'LIMIT':
                    price_str = input("Enter price: ").strip()
                    if price_str.lower() in ['exit', 'quit']: break
                    try:
                        price = float(price_str)
                    except ValueError:
                        print("Invalid price! Must be a number.\n")
                        continue
                
                # Validate inputs
                errors = validate_order_inputs(symbol, side, order_type, quantity, price)
                if errors:
                    print("\nValidation Errors:")
                    for err in errors:
                        print(f" - {err}")
                    print("\nPlease try again.\n")
                    continue
                
                # Place order
                print("\nProcessing order...")
                if order_type == 'MARKET':
                    response = place_market_order(client, symbol, side, quantity)
                else:
                    response = place_limit_order(client, symbol, side, quantity, price)
                
                # Print clean response
                print_order_response(response)
                
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                print("Please check the logs for more details.\n")
                
            # Ask if user wants to place another order
            again = input("Place another order? (y/n): ").strip().lower()
            if again != 'y':
                break
                
    except Exception as e:
        print(f"\nInitialization failed: {e}")
        print("Check your .env file and network connection.")
        sys.exit(1)
        
    print("\nThank you for using the Trading Bot!")

if __name__ == "__main__":
    main()
