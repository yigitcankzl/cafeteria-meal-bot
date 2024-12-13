import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Function to fetch and process today's meal list
def get_today_meals():
    url = "http://www.sksdb.hacettepe.edu.tr/YemekListesi.xml"
    response = requests.get(url)
    response.raise_for_status()  # Error checking

    root = ET.fromstring(response.content)
    today_date = datetime.now().strftime("%d.%m.%Y")

    meal_list = []
    # Check each 'gun' (day) element in the XML
    for day in root.findall('.//gun'):
        date = day.find('tarih').text
        if today_date in date:
            meals = day.find('yemekler')
            for meal in meals.findall('yemek'):
                meal_list.append(meal.text)

    return meal_list
