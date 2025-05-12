import gspread
from google.oauth2.service_account import Credentials
import json
import os
from datetime import datetime, timezone
import logging

logger = logging.getLogger("stripe_webhook")
logging.basicConfig(level=logging.INFO)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

def get_sheet():
    try:
        service_account_info = json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))

        if "\\n" in service_account_info["private_key"]:
            service_account_info["private_key"] = service_account_info["private_key"].replace("\\n", "\n")

        credentials = Credentials.from_service_account_info(
            service_account_info,
            scopes=SCOPES
        )

        client = gspread.authorize(credentials)

        return client.open("Donation Audit Sheet").worksheet(os.getenv("AUDIT_WORKSHEET"))

    except Exception as e:
        logger.error(f"Failed to get sheet: {e}")


def log_donation_to_sheet(
        email: str, 
        full_name: str,
        postcode: str,
        address_line_one: str,
        address_line_two: str,
        amount: float,
        gift_aid: bool,
        payment_type: str,
    ):
    try:
        sheet = get_sheet()
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        row = [
            timestamp,
            email,
            full_name,
            postcode,
            address_line_one,
            address_line_two,
            f"£{amount:.2f}",
            "Yes" if gift_aid else "No",
            payment_type.title()
        ]        
        sheet.append_row(row)
    except Exception as e:
         logger.error(f"Failed to append row: {e}")