import boto3
import os

def send_management_email(to_email: str, portal_url: str):
    client = boto3.client(
        "ses",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    response = client.send_email(
        Source="alexanderpope27@gmail.com",
        Destination={
            "ToAddresses": [to_email],
        },
        Message={
            "Subject": {
                "Data": "Manage Your Dream Renewables Donation",
            },
            "Body": {
                "Text": {
                    "Data": f"Hello!\n\nThank you for supporting Dream Renewables.\n\nYou can manage your donation here: {portal_url}\n\nThank you for being part of the change!",
                },
                "Html": {
                    "Data": f"""
                    <html>
                        <body>
                            <h3>Manage Your Dream Renewables Donation</h3>
                            <p>Thank you for supporting our mission! You can manage your donation anytime by visiting the link below:</p>
                            <p><a href="{portal_url}">Manage Your Donation</a></p>
                            <p>Thank you again for your generosity!</p>
                        </body>
                    </html>
                    """,
                },
            },
        },
    )

    return response