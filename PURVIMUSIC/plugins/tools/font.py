import random
from nickname_generator import generate
from pyrogram import Client, filters
from PURVIMUSIC import app

# Function to generate stylish nicknames using the nickname-generator library
def get_stylish_names(name):
    stylish_names = []
    for _ in range(10):  # Generate 10 different stylish names
        # Here, we're using the nickname-generator library to create stylish names
        # You can modify this line to create more stylized names based on your needs
        nickname = generate()
        stylish_names.append(nickname)
    return stylish_names

@app.on_message(filters.text)
def suggest_nicknames(client, message):
    # Get the text from the user (the name)
    name = message.text.strip()

    # If the name is empty or too short, ask the user to provide a valid name
    if not name or len(name) < 2:
        message.reply("Please provide a valid name!")
        return

    # Get random stylish names for the provided name
    stylish_names = get_stylish_names(name)

    if stylish_names:
        # Send the list of 10 stylish names as a message to the user
        response = "Here are 10 stylish nicknames for you:\n\n"
        response += "\n".join(stylish_names)
        message.reply(response)
    else:
        message.reply("Sorry, I couldn't fetch stylish nicknames at the moment. Please try again later.")
