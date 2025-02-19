import random
import requests
from pyrogram import Client, filters
from PURVIMUSIC import app

# URL for Fancy Text Generator API from RapidAPI (replace with actual URL after signing up)
FONT_API_URL = "https://fancy-text-generator1.p.rapidapi.com/fancy-text"  # Example, you need to replace it
API_KEY = "1fd96a58c9mshe95230528fa4667p16c1d2jsn1df774c94c22"  # Replace with your API key from RapidAPI

@app.on_message(filters.text)
def insert_name(client, message):
    name = message.text.strip()
    if not name:
        message.reply("Please send a name.")
        return

    # Call the Fancy Text Generator API to get a random font
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "fancy-text-generator1.p.rapidapi.com"
    }

    # Make API request
    try:
        response = requests.get(FONT_API_URL, headers=headers, params={"text": name})
        if response.status_code == 200:
            # Extract the random font from the response
            font_data = response.json()  # Assuming the response is in JSON format
            if font_data and 'fancy_text' in font_data:
                random_font = font_data['fancy_text']

                # Insert the name in the middle of the font (modify this logic based on the API response structure)
                mid_point = len(random_font) // 2
                new_text = random_font[:mid_point] + name + random_font[mid_point:]

                # Send the modified text back
                message.reply(new_text)
            else:
                message.reply("Could not retrieve a random font.")
        else:
            message.reply("Failed to fetch font from the generator.")
    except Exception as e:
        message.reply(f"Error while fetching font: {e}")
