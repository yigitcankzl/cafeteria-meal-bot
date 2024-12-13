Cafeteria Meal WhatsApp Notifier

This project sends the daily cafeteria meal list to a specified WhatsApp number using Twilio's API. The meal list is fetched from a public XML file provided by Hacettepe University's cafeteria service.

Project Structure

cafeteria_meal_bot_project/
│
├── .env                  # Environment variables (Twilio credentials and phone numbers)
├── .gitignore            # Git ignore file (for excluding sensitive files like .env)
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
├── main.py               # Main entry point of the application
│
├── modules/
│   ├── __init__.py       # (Optional, usually left empty)
│   ├── meal_fetcher.py   # Fetches and processes today's meal list
│   ├── whatsapp_sender.py # Sends the meal list via WhatsApp using Twilio
│   └── config_loader.py  # Loads environment variables from .env file

Prerequisites

Before running this project, you need the following:

1. Twilio Account: You need a Twilio account and WhatsApp sandbox credentials.
   - Sign up at Twilio (https://www.twilio.com/).
   - Set up WhatsApp messaging as per Twilio's instructions.

2. Python 3.x: This project is built using Python. Install Python from here (https://www.python.org/downloads/) if you don't have it yet.

3. Install Required Packages:
   - You can install the required Python packages by running:
   pip install -r requirements.txt

4. Create a .env File: Store your Twilio credentials and WhatsApp numbers in a .env file in the project root. The .env file should look like this:
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   FROM_WHATSAPP=whatsapp:+14155238886  # Twilio sandbox number
   TO_WHATSAPP=whatsapp:+90XXXXXXXXXX  # Your target WhatsApp number

How to Run the Project

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Ensure you have installed all dependencies using pip install -r requirements.txt.
4. Make sure the .env file is in place with your Twilio credentials and WhatsApp numbers.
5. Run the main.py file:
   python main.py

This will fetch the meal list for today from the XML file and send it as a message to the specified WhatsApp number.

How It Works

1. Fetching Meal List: The program fetches today's cafeteria meal list from the Hacettepe University public XML feed.
2. Sending Message: The meal list is then sent as a message to the target WhatsApp number using Twilio's API.

Dependencies

- requests: To fetch data from the public XML feed.
- twilio: To send the message via Twilio API.
- python-dotenv: To securely load environment variables from the .env file.

You can install all dependencies by running:
pip install -r requirements.txt

License

This project is licensed under the MIT License - see the LICENSE file for details.
