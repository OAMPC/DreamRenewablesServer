import stripe
from os import getenv

stripe.api_key = getenv("STRIPE_SECRET_KEY")

def create_checkout_session(amount_in_pence: int, payment_type: str, cancel_url: str):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription" if payment_type == "monthly" else "payment",
        line_items=[{
            "price_data": {
                "currency": "gbp",
                "unit_amount": amount_in_pence,
                "product_data": {
                    "name": "Monthly Donation to Dream Renewables" if payment_type == "monthly" else "One-Time Donation to Dream Renewables",
                },
                "recurring": {"interval": "month"} if payment_type == "monthly" else None,
            },
            "quantity": 1,
        }],
        success_url=getenv("FRONTEND_URL") + "/payment-success",
        cancel_url=getenv("FRONTEND_URL") + cancel_url,
    )
    return session
