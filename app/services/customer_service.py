from gateways.stripe_gateway import create_customer_session
from gateways.aws_ses_gateway import send_management_email

def email_customer_management_url(data: dict):
    customer_email = data.get("email")
    if not customer_email:
        raise ValueError("Email is required")
    
    customer_session_url = create_customer_session(customer_email)    
    send_management_email(customer_email, customer_session_url)

    return customer_session_url
