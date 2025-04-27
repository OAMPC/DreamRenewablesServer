from fastapi import APIRouter, Request
from services.webhook_service import handle_stripe_event

router = APIRouter()

@router.post("/api/v1/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    signature_header = request.headers.get("stripe-signature")

    try:
        result = handle_stripe_event(payload, signature_header)
        return {"status": result}
    except Exception as e:
        print("Webhook error:", e)
        return {"status": "error", "detail": str(e)}
