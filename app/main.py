from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.customer_controller import router as customer_controller
from controllers.payment_controller import router as payment_router
from controllers.webhook_controller import router as webhook_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_router)
app.include_router(webhook_router)
app.include_router(customer_controller)