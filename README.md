# 🐼 Panda Bot

A delightful Telegram bot that delivers adorable panda pictures to your chats, built with Python!

## Features
- Automatic panda picture delivery every 30 minutes
- Daily panda update at 12:00 PM
- On-demand pandas with `/panda` command
- Interactive commands system
- Echo functionality for text messages

## Commands
- `/start` - Start the bot
- `/help` - Show help message
- `/panda` - Get a random panda picture

## Setup
```bash
# Clone repository
git clone https://github.com/yourusername/panda-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install python-telegram-bot

# Configure environment variables
cp .env.example .env

# Create 'pandas' folder and add your panda images
mkdir pandas

# Run the bot
python main.py
```

## Technologies
- Python 3.x
- python-telegram-bot
- AsyncIO

## Requirements
- Python 3.7 or higher
- Telegram Bot Token
- Collection of panda images in 'pandas' folder

## License
MIT License

## Contributing
Feel free to open issues and pull requests!
