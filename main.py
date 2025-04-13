from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import stripe
import os
from helpers import convert_to_pence

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
    amount_in_pence = convert_to_pence(data.get("amountInPounds"))
    paymentType = data.get("paymentType")
    cancel_url = data.get("cancelUrl")

    print(data)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription" if paymentType == "monthly" else "payment",
            line_items=[{
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": amount_in_pence,
                    "product_data": {
                        "name": "Dream Renewables" if paymentType == "monthly" else "Donation",
                    },
                    "recurring": {"interval": "month"} if paymentType == "monthly" else None,
                },
                "quantity": 1,
            }],
            success_url=os.getenv("FRONTEND_URL") + "/payment-success",
            cancel_url=os.getenv("FRONTEND_URL") + f"{cancel_url}",
        )
        return {"url": session.url}
    except Exception as e:
        return {"error": str(e)}
