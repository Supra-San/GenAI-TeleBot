from config.config import OPENAI_API_KEY, TELEGRAM_API_KEY  # Import API keys from configuration file
import telebot  # Import Telegram bot library
import openai  # Import OpenAI library
import requests  # Import requests module for handling HTTP requests
import logging  # Import logging module for debugging and error handling

# Setup logging configuration to log messages with timestamps
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize OpenAI API client using new API format
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize Telegram bot with API key
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# Function to generate an image using OpenAI API
def generate_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",  # Specify the model to use (DALL·E 3)
            prompt=prompt,  # User-provided prompt for image generation
            size="1024x1024",  # Define the image size
            n=1,  # Number of images to generate
        )
        return response.data[0].url  # Return the generated image URL
    except Exception as e:
        logging.error(f"Error generating image: {e}")  # Log any errors that occur
        return None  # Return None if an error occurs

# Function to generate text using OpenAI API
def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT model
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},  # System role
                {"role": "user", "content": prompt}  # User prompt input
            ],
            temperature=0.7,  # Adjust response randomness
            max_tokens=2048  # Set the maximum response length
        )
        return response.choices[0].message.content.strip()  # Return the generated text
    except Exception as e:
        logging.error(f"Error generating text: {e}")  # Log any errors that occur
        return "⚠️ An error occurred while generating text."  # Return error message

# Command: Start - Sends a welcome message when user starts the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "🤖 *Welcome to GenAI Tele-Bot!*\n"
        "You can generate AI-generated images and text using the following commands:\n"
        "📷 `/generate-image <prompt>` - Generate an AI image\n"
        "📝 `/generate-text <prompt>` - Generate AI text"
    )
    bot.reply_to(message, welcome_message, parse_mode="Markdown")  # Send welcome message in Markdown format

# Command: Generate Image - Handles image generation request
@bot.message_handler(func=lambda msg: msg.text.startswith('/generate-image '))
def handle_generate_image(message):
    prompt = message.text[len('/generate-image '):].strip()  # Extract prompt from command
    
    if not prompt:  # Check if prompt is empty
        bot.reply_to(message, "⚠️ Please provide a description for the image.")
        return

    bot.reply_to(message, "⏳ *Generating image, please wait...*", parse_mode="Markdown")
    
    image_url = generate_image(prompt)  # Call image generation function
    if image_url:
        try:
            bot.send_photo(message.chat.id, image_url, caption="🖼️ *Here is your AI-generated image!*", parse_mode="Markdown")
        except Exception as e:
            logging.error(f"Error sending image: {e}")
            bot.reply_to(message, "⚠️ Failed to send the generated image.")
    else:
        bot.reply_to(message, "❌ Error generating image.")

# Command: Generate Text - Handles text generation request
@bot.message_handler(func=lambda msg: msg.text.startswith('/generate-text '))
def handle_generate_text(message):
    prompt = message.text[len('/generate-text '):].strip()  # Extract prompt from command
    
    if not prompt:  # Check if prompt is empty
        bot.reply_to(message, "⚠️ Please provide a text prompt.")
        return

    bot.reply_to(message, "⏳ *Generating text, please wait...*", parse_mode="Markdown")
    
    text_response = generate_text(prompt)  # Call text generation function
    bot.reply_to(message, f"📝 {text_response}")  # Send generated text response

# Default handler for invalid commands
@bot.message_handler(func=lambda message: True)
def handle_invalid_command(message):
    bot.reply_to(message, "❌ Invalid command. Use `/generate-image` or `/generate-text`.", parse_mode="Markdown")

# Run bot and listen for messages
logging.info("🤖 Bot is running...")
bot.polling()
