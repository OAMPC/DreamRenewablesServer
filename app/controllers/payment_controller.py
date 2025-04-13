from fastapi import APIRouter, Request
from services.payment_service import generate_checkout_session

router = APIRouter()

@router.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    data = await request.json()
    try:
        session_url = generate_checkout_session(data)
        return {"url": session_url}
    except Exception as e:
        return {"error": str(e)}
