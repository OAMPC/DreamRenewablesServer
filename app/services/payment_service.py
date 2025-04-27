from gateways.stripe_gateway import create_checkout_session
from utils.helpers import convert_to_pence

def generate_checkout_session(data: dict):
    amount_in_pence = convert_to_pence(data.get("amountInPounds"))
    payment_type = data.get("paymentType")
    cancel_url = data.get("cancelUrl")
    
    session = create_checkout_session(amount_in_pence, payment_type, cancel_url)
    return session.url
