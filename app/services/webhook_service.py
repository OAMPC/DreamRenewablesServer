from gateways.sheets_gateway import log_donation_to_sheet
from gateways.stripe_gateway import verify_stripe_signature
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

    if event_type == "checkout.session.completed":
        customer_details = data.get("customer_details", {})
        address = customer_details.get("address", {})

        email = customer_details.get("email", "[no email]")

        postal_code = address.get("postal_code", "[no postcode]")
        address_line_one = address.get("line1", "[no address line one]")
        address_line_two = address.get("line2", "[no address line two]")


        metadata = data.get("metadata", {})
        gift_aid = metadata.get("gift_aid", "false") == "true"

        custom_fields = data.get("custom_fields", [])
        full_name = next((field['text']['value'] for field in custom_fields if field['key'] == 'full_name'), "[no name]")

        amount = data.get("amount_total", 0) / 100
        payment_type = "monthly" if data.get("mode") == "subscription" else "one-time"

        log_donation_to_sheet(
            email=email,
            full_name=full_name,
            postcode=postal_code,
            address_line_one=address_line_one,
            address_line_two=address_line_two,
            amount=amount,
            gift_aid=gift_aid,
            payment_type=payment_type,
        )        
        return "checkout.session.completed processed"

    return f"Ignored event: {event_type}"
