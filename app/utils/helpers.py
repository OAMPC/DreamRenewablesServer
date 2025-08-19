from decimal import Decimal


def convert_to_pence(amount):
    return int(amount * 100)

def format_amount(amount):
    try:
        value = Decimal(amount)
        return f"£{value:.2f}"
    except Exception:
        return f"£{amount}"