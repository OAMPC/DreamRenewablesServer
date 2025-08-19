import boto3
import os
from utils.helpers import format_amount

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

def send_thank_you_email(to_email: str, full_name: str, amount: str, payment_type: str, customer_session_url: str):
    client = boto3.client(
        "ses",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    first_name = full_name.split()[0]
    formatted_amount = format_amount(amount=amount)
    one_time_message = {
        "Subject": {
            "Data": "Thank you for your gift to Dream Renewables",
        },
        "Body": {
            "Html": {
                "Data": f"""
                <html>
                <body style="margin:0; padding:0; font-family: Arial, sans-serif; background:#f9f9f9;">
                  <table align="center" cellpadding="0" cellspacing="0" width="600" 
                         style="background:#ffffff; margin:20px auto; padding:20px; 
                                border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1);">
                    <tr>
                      <td align="center" style="padding-bottom:20px;">
                        <img src="https://dream-renewables-server-cdaa038ff427.herokuapp.com/app/static/images/dr_logo.png" 
                             alt="Dream Renewables" width="180" style="display:block;" />
                      </td>
                    </tr>
                    <tr>
                      <td style="font-size:16px; color:#333; line-height:1.5; padding:0 20px;">
                        <p>Dear {first_name},</p>
                        <p>Thank you so much for your generous gift of {formatted_amount} to Dream Renewables. Your support means the world to us.</p>
                        <p>Because of you, we can bring renewable energy to vulnerable communities in Ghana—providing the power for life-saving vaccines, transforming access to education, and enabling clean, safe water. Even a small amount of energy can change lives, and your gift makes that possible.</p>
                        <p>Your donation has been received and is being processed through our UK charity partner, Dream Big Ghana Foundation, which ensures our projects meet the highest standards of accountability and impact.</p>
                        <p>If you have any questions or feedback, simply reply to this email and we’ll be in touch within five working days.</p>
                        <p>With gratitude,<br/>The Dream Renewables Team</p>
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
    }

    monthly_message = {
        "Subject": {
            "Data": "Thank you for your monthly commitment to Dream Renewables",
        },
        "Body": {
            "Html": {
                "Data": f"""
                <html>
                <body style="margin:0; padding:0; font-family: Arial, sans-serif; background:#f9f9f9;">
                  <table align="center" cellpadding="0" cellspacing="0" width="600" 
                         style="background:#ffffff; margin:20px auto; padding:20px; 
                                border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1);">
                    <tr>
                      <td align="center" style="padding-bottom:20px;">
                        <img src="https://dream-renewables-server-cdaa038ff427.herokuapp.com/app/static/images/dr_logo.png" 
                             alt="Dream Renewables" width="180" style="display:block;" />
                      </td>
                    </tr>
                    <tr>
                      <td style="font-size:16px; color:#333; line-height:1.5; padding:0 20px;">
                        <p>Dear {first_name},</p>
                        <p>Thank you for choosing to make a monthly gift of {formatted_amount} to Dream Renewables. Your ongoing support is truly powerful.</p>
                        <p>Your generosity fuels renewable energy projects that bring lasting change to communities in Ghana—from powering refrigerators that store vaccines, to lighting classrooms, to pumping safe drinking water. Month by month, you’re creating sustainable impact.</p>
                        <p>Your donations are processed through our UK charity partner, Dream Big Ghana Foundation, which oversees our work to ensure transparency and effectiveness.</p>
                        <p>If at any time you’d like to update your monthly gift, you can manage it easily through your secure Stripe portal here:</p>
                        <p style="text-align:center; margin:30px 0;">
                          <a href="{customer_session_url}" 
                             style="background:#2d7a5f; color:#ffffff; padding:12px 24px; 
                                    text-decoration:none; border-radius:4px; font-weight:bold;">
                             Manage Your Donation
                          </a>
                        </p>
                        <a href="https://dreamrenewables.org/manage-your-donations">
                        <p>This link will last 24 hours for security purposes and another link can be requested from our website here</p>
                        </a>
                        <p>And of course, if you ever have questions or feedback, just reply to this email, our team will get back to you within five working days.</p>
                        <p>With heartfelt thanks,<br/>The Dream Renewables Team</p>
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
    }

    response = client.send_email(
        Source="hello@dreamrenewables.org",
        Destination={
            "ToAddresses": [to_email],
        },
         Message=monthly_message if payment_type == "monthly" else one_time_message 
    )

    return response