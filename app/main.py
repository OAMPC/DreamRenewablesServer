from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.payment_controller import router as payment_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_router)
