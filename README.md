# Generative AI TeleBot

This Telegram bot integrates OpenAI's API to generate AI-powered images and text based on user prompts. The bot allows users to:<br/>
✅ Generate images using DALL·E 3 by providing a text prompt.<br/>
✅ Generate text responses using GPT-3.5-Turbo.<br/>
✅ Interact with AI through a simple Telegram interface.

## Features
✅ Image Generation: Users can request AI-generated images based on text prompts.<br/>
✅ Text Generation: Users can generate AI-based responses for creative or informational purposes.<br/>
✅ User-Friendly Commands: Simple /generate-image and /generate-text commands for easy interaction.<br/>
✅ Error Handling & Logging: Built-in error handling and logging for better stability.<br/>
✅ Secure API Key Management: API keys are stored in a separate config module.


## Installation
1. Clone the repository:
```bash
git clone https://github.com/Supra-san/GenAI-Telebot.git
```

2. Navigate to the project directory:
```bash
cd GenAI-TeleBot
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set Up API Keys
Edit config/config.py and replace placeholders with actual API keys.
```bash
OPENAI_API_KEY = "your_openai_api_key"
TELEGRAM_API_KEY = "your_telegram_api_key"
```

5. Run the Bot
```bash
python app.py
```
## Error Handling
Invalid Commands:
```bash
❌ Invalid command. Use /generate-image or /generate-text.
```

API Errors:
```bash
❌ Error generating image.
```

Network Issues:
```bash
⚠️ Failed to retrieve the image.
```

## Future Improvements

Support for different image sizes and styles.<br/>
Improved UI with inline buttons for better user interaction.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
OpenAI for the API used in this project.
Telegram for providing a platform for building interactive bots

> [!NOTE]
> Feel free to modify it according to your specific features or goals! If you need further assistance, just let me know.
