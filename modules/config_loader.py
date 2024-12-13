from dotenv import load_dotenv
import os

# Function to load environment variables from .env file
def get_config():
    load_dotenv()
    return {
        'ACCOUNT_SID': os.getenv('ACCOUNT_SID'),
        'AUTH_TOKEN': os.getenv('AUTH_TOKEN'),
        'FROM_WHATSAPP': os.getenv('FROM_WHATSAPP'),
        'TO_WHATSAPP': os.getenv('TO_WHATSAPP'),
    }
