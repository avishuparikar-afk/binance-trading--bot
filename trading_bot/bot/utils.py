def print_order_response(response: dict):
    """Print the order response nicely to the console."""
    print("\n" + "="*40)
    print("ORDER RESPONSE SUMMARY")
    print("="*40)
    for key, value in response.items():
        print(f"{key:20}: {value}")
    print("="*40 + "\n")
