from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import stripe
import os

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    data = await request.json()
    amount = data.get("amount")  # in pounds
    is_monthly = data.get("isMonthly")
    print(data)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription" if is_monthly else "payment",
            line_items=[{
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": int(amount * 100),  # Convert to pence
                    "product_data": {
                        "name": "Donation",
                    },
                    "recurring": {"interval": "month"} if is_monthly else None,
                },
                "quantity": 1,
            }],
            success_url=os.getenv("FRONTEND_URL") + "/payment-success",
            cancel_url=os.getenv("FRONTEND_URL") + "/payment-cancel",
        )
        return {"url": session.url}
    except Exception as e:
        return {"error": str(e)}
