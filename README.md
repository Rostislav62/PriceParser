# PriceParser: Web Scraper with Telegram Notifications

## Overview

### Problem
Internet stores and freelancers often need to monitor product prices on competitor websites, but manual tracking is time-consuming and inefficient.

### Solution
PriceParser is a Python-based web scraper that collects product prices from a target website, tracks changes, and sends automated reports via Telegram, with optional email notifications.

### Impact
Saves time for businesses and freelancers by automating price monitoring, providing real-time updates, and enabling quick decision-making based on market trends.

## About the Project
PriceParser is a lightweight web scraping tool built with Python, designed to extract product prices from a website (e.g., a demo online store) and notify users of changes via Telegram. It uses BeautifulSoup for parsing, SQLite for data storage, and aiogram for Telegram notifications. The project showcases my expertise in web scraping, automation, and bot development.

## Features
- **Web Scraping**: Extracts product names and prices from a specified website.
- **Price Tracking**: Stores data in SQLite to detect price changes.
- **Telegram Notifications**: Sends reports to a Telegram chat with product details and price changes.
- **Periodic Updates**: Runs hourly checks using the schedule library.
- **Optional Email Notifications**: Sends reports via SMTP (e.g., Gmail).
- **Subscription Model**: Users can subscribe/unsubscribe to notifications via Telegram commands.


## How to Work with PriceParser

### Access the Bot
Find the bot in Telegram (e.g., t.me/PriceParserGoodBot, or @PriceParserGoodBot) or run locally (see Setup Instructions).

### User Workflow
1. Start Interaction:
  - Send /start to receive a welcome message and instructions.
2. Subscribe to Notifications:
  - Send /subscribe to receive hourly price reports.
  - Send /unsubscribe to stop notifications.
3. Request Report:
  - Send /report to get the latest product prices and changes.
4. Receive Updates:
  - Hourly reports are sent to subscribed users via Telegram.
  - Optional email reports (if configured).


### Example Usage
- Send /start: "Welcome to PriceParser! Use /subscribe to receive price updates or /report for the latest prices."
- Send /subscribe: "You are now subscribed to hourly price reports."
- Send /report: "Product: Widget A, Price: $10.00 (no change); Product: Widget B, Price: $15.00 (down $1.00)."
- Receive hourly Telegram message with price updates.

### Notes
- The parser targets a demo store (e.g., https://scrapeme.live/shop/). Update the URL in config.py for other sites.
- Email notifications require SMTP configuration in .env.
- Price changes are highlighted in reports (e.g., "up $1.00" or "down $0.50").

## Setup Instructions

### Create Virtual Environment
1. Clone the repository:
    ```bash
   git clone https://github.com/Rostislav62/PriceParser.git
   cd PriceParser
2. Create and activate a virtual environment:
    ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
3. Install dependencies:
    ```bash
   pip install -r requirements.txt

### Create Database
1. Run the initialization script to create the SQLite database:
    ```bash
   python init_db.py


### Configure Telegram and Email
1. Create a .env file in the project root:
BOT_TOKEN=your_telegram_bot_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_email_password

- Replace your_telegram_bot_token with the token from BotFather.
- For email, configure SMTP settings (e.g., Gmail credentials).


### Run the Parser
1. Start the bot and parser:
    ```bash
   python main.py


## API Keys
The bot uses external services::
- Telegram Bot API: Obtain token from BotFather.
- MTP Service: Configure via .env (e.g., Gmail SMTP).


## Project Structure
- `main.py` — Bot initialization and scheduler setup.
- `config.py` — Configuration (Telegram token, SMTP settings).
- `utils.py` — Database and parsing utilities.
- `handlers.py` — Telegram command handlers.
- `services/` — API-specific modules:
  - `parser.py`:  Web scraping logic.
  - `notifier.py`: Telegram and email notification logic.
- `models.py`: SQLite models for prices and subscriptions.
- `init_db.py`: Database initialization script.

## Technologies
- **Python 3.8**: Core language.
- **aiogram 2.21**: Telegram Bot API framework.
- **BeautifulSoup**: HTML parsing.
- **smtplib**: Email notifications.
- **requests**: HTTP requests.
- **schedule**: Periodic tasks.
- **peewee**: SQLite ORM.
- **python-dotenv**: Environment variables.
- **Git**: Version control.

## Author
Rostislav — Full-stack developer specializing in bot development and API integration. This project is part of my portfolio, showcasing expertise in Telegram bots, NLP, and data automation.

## License
MIT License