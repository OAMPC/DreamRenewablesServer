from fastapi import APIRouter, Request
from services.customer_service import email_customer_management_url

router = APIRouter()

@router.post("/api/v1/email-customer-stripe-management-url")
async def email_customer_stripe_management_url(request: Request):
    data = await request.json()
    try:
        email_customer_management_url(data)
        return {"status": "200 success"}
    except Exception as e:
        return {"error": str(e)}, 500
