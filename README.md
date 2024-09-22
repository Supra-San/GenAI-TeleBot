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
cd GenAI-TeleBot
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
- Make sure your api_keys are filled in correctly

```bash
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
TELEGRAM_API_TOKEN = "YOUR_TELEGRAM_API_KEY"
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
