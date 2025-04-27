from gateways.stripe_gateway import verify_stripe_signature
import json
import logging

logger = logging.getLogger("stripe_webhook")
logging.basicConfig(level=logging.INFO)

def handle_stripe_event(payload: bytes, signature_header: str) -> str:
    try:
        event = verify_stripe_signature(payload, signature_header)
    except Exception as e:
        logger.error(f"Webhook signature verification failed: {str(e)}")
        raise

    event_type = event.get("type", "unknown")
    data = event.get("data", {}).get("object", {})

    logger.info(f"Received Stripe event: {event_type}")

    if event_type == "checkout.session.completed":
        customer_details = data.get("customer_details", {})
        email = customer_details.get("email", "[no email]")
        amount = data.get("amount_total", 0)
        metadata = data.get("metadata", {})

        logger.info(f"Payment completed")
        logger.info(f" - Email: {email}")
        logger.info(f" - Amount: £{amount/100:.2f}")
        logger.info(f" - Metadata: {json.dumps(metadata)}")

        # TODO: Save donation, send thank you, etc.
        return "checkout.session.completed processed"

    logger.warning(f"Ignored unexpected event type: {event_type}")
    return f"Ignored event: {event_type}"
