from modules.meal_fetcher import get_today_meals
from modules.whatsapp_sender import send_whatsapp_message

def main():
    # Get today's meals
    meals = get_today_meals()

    # Create the message
    if meals:
        message = f"Today's meals:\n" + "\n".join(f"- {meal}" for meal in meals)
    else:
        message = "No meal list found for today."

    # Send the message via WhatsApp
    send_whatsapp_message(message)

if __name__ == "__main__":
    main()
