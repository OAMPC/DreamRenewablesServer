from gateways.stripe_gateway import verify_stripe_signature

def handle_stripe_event(payload: bytes, signature_header: str) -> str:
    event = verify_stripe_signature(payload, signature_header)

    event_type = event["type"]
    data = event["data"]["object"]

    print(f"Received Stripe event: {event_type}")

    if event_type == "checkout.session.completed":
        email = data.get("customer_email")
        amount = data.get("amount_total")
        metadata = data.get("metadata", {})

        print(f"Payment from {email} for {amount}p")
        print(f"Metadata: {metadata}")

        # TODO: Save donation, send thank you, etc.
        return "checkout.session.completed processed"

    return f"Ignored event: {event_type}"
