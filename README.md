# DreamRenewablesServerless

## Setup

1. FastApi

   1. Install Python - this was written using 3.11.2
   2. Create a venv in the root of repo: `python -m venv .venv`
   3. Activate your venv:

      ```bash
      # In cmd.exe
      source .venv\Scripts\activate.bat
      # In PowerShell
      source .venv\Scripts\Activate.ps1
      # In Git Bash
      source .venv/Scripts/activate
      # In Linux or Macos
      source .venv/bin/activate
      ```

   4. Install Python requirements: `pip install -r requirements.txt`
   5. Create a .env file in the root of the repo and obtain the keys from a maintainer.

2. Stripe
   1. Install the [Stripe Cli](https://docs.stripe.com/stripe-cli) and login
   2. Set Stripe webhooks to ping to your local instance: `stripe listen --forward-to localhost:8000/api/v1/webhook`
   3. Save your webhook signing secret as a secret in .env called `STRIPE_WEBHOOK_SECRET`

## Running the app

1. Run the app: `fastapi dev app/main.py`
2. You can send events to `webhook` with `stripe trigger checkout.session.completed`

## Related Repositories

| Name                                                                                      | Description                                                   |
| :---------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| [Dream Renewables Cms](https://github.com/OAMPC/DreamRenewablesCms)                       | The Content Management System for this web application        |
| [Dream Renewables Infrastructure](https://github.com/OAMPC/DreamRenewablesInfrastructure) | The Terraform for this web applications required architecture |
| [Dream Renewables Frontend](https://github.com/OAMPC/DreamRenewablesFrontend)             | React code for this web application                           |
