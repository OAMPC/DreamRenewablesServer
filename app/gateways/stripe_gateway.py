import stripe
from os import getenv

stripe.api_key = getenv("STRIPE_SECRET_KEY")
WEBHOOK_SECRET = getenv("STRIPE_WEBHOOK_SECRET")

def create_checkout_session(amount_in_pence: int, payment_type: str, cancel_url: str, gift_aid_donation: bool):
    metadata = {
        "gift_aid": str(gift_aid_donation).lower()
    }
    
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
        metadata=metadata,
        payment_intent_data={"metadata": metadata} if payment_type == "oneTime" else None,
        subscription_data={"metadata": metadata} if payment_type == "monthly" else None,
    )
    return session

def verify_stripe_signature(payload: bytes, sig_header: str) -> dict:
    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=WEBHOOK_SECRET
        )
        return event
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        print("Stripe webhook signature invalid: ", e)
        raise