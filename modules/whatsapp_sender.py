from twilio.rest import Client
from modules.config_loader import get_config

# Function to send a WhatsApp message using Twilio
def send_whatsapp_message(message):
    config = get_config()
    client = Client(config['ACCOUNT_SID'], config['AUTH_TOKEN'])

    # Send the message via WhatsApp
    client.messages.create(
        body=message,
        from_=config['FROM_WHATSAPP'],
        to=config['TO_WHATSAPP']
    )
