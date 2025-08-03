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
        Source="noreply@dreamrenewables.org",
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
                <body style="margin:0; padding:0; font-family: Arial, sans-serif; background:#f9f9f9;">
                    <table align="center" cellpadding="0" cellspacing="0" width="600" style="background:#ffffff; margin:20px auto; padding:20px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1);">
                    <tr>
                        <td align="center" style="padding-bottom:20px;">
                        <img src="https://dream-renewables-server-cdaa038ff427.herokuapp.com/app/static/images/dr_logo.png" alt="Dream Renewables" width="180" style="display:block;" />
                        </td>
                    </tr>
                    <tr>
                        <td style="font-size:16px; color:#333; line-height:1.5; padding:0 20px;">
                        <p>Thank you for supporting our mission! You can manage your donation anytime by visiting the link below:</p>
                        <p style="text-align:center; margin:30px 0;">
                            <a href="{portal_url}" style="background:#2d7a5f; color:#ffffff; padding:12px 24px; text-decoration:none; border-radius:4px; font-weight:bold;">Manage Your Donation</a>
                        </p>
                        <p>Thank you again for your generosity and for being part of the change!</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="font-size:12px; color:#777; text-align:center; padding-top:30px;">
                        <p>Dream Renewables, Ghana & London, UK</p>
                        <p><a href="https://dreamrenewables.org" style="color:#2d7a5f;">dreamrenewables.org</a></p>
                        </td>
                    </tr>
                    </table>
                </body>
                </html>
                """
            }
            },
        },
    )

    return response