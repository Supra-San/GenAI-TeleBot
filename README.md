# Generative AI TeleBot

This repository contains a Telegram bot that integrates OpenAI's image generation and text generation capabilities. Users can generate images based on textual prompts and create paragraphs of text by inputting simple commands. The bot is designed to be user-friendly and showcases the potential of generative AI in interactive applications.

## Features
- Generate images using OpenAI's DALL-E model from user prompts.
- Create paragraphs of text based on user input.
- Easy to use with simple commands.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Supra-san/GenAI-Telebot.git
```

2. Navigate to the project directory:
```bash
git clone https://github.com/Supra-san/GenAI-Telebot.git
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
- Store your API keys in a separate file within the config folder.
- Ensure your config/api_keys.py file contains the following:

```bash
TELEGRAM_API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

## Usage

```bash
python app.py
```

- Use the following commands in Telegram:
  + /generate-image <prompt> to generate an image.
  + /generate-text <prompt> to create a paragraph of text.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
OpenAI for the API used in this project.
Telegram for providing a platform for building interactive bots

> [!NOTE]
> Feel free to modify it according to your specific features or goals! If you need further assistance, just let me know.
