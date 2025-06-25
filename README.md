# PriceParser: Telegram Bot + Web Interface for Price Monitoring

## Overview

### Problem
Businesses and freelancers often need to monitor product prices (e.g., competitors), but manual tracking is time-consuming and inefficient.

### Solution
**PriceParser** is a Python-powered price tracking tool that scrapes data from websites, stores price history, detects changes, and sends updates via Telegram or renders them in a web interface using FastAPI + Jinja2.

### Impact
Automates the entire price-monitoring process, saves time, and helps users react faster to market changes through visual reports and timely alerts.

---

## About the Project

**PriceParser** is a lightweight full-stack solution that includes:

- 🤖 A Telegram bot (built with `aiogram`) for notifications and user commands.
- 🌐 A FastAPI web interface with HTML templates for viewing prices and trends.
- 📈 Historical graphs for each product (7-day timeline).
- 💬 Flexible commands like `/report`, `/reportdelta`, `/history`, `/notifychange`.
- ⚙️ Per-user preference: receive all prices or only price changes.

The tool uses `BeautifulSoup` and `peewee` for scraping and storage, `matplotlib` for graph generation, and `schedule` for periodic tasks.

---

## Features

- **Web Scraping**: Extracts product names and prices from a target source.
- **Price History**: Stores daily prices in SQLite for comparisons.
- **Telegram Notifications**: Sends hourly reports to subscribed users.
- **Subscription Model**: Users can subscribe/unsubscribe to notifications via Telegram commands.
- **Periodic Updates**: Runs hourly checks using the schedule library.
- **Selective Alerts**: Option to receive all updates or only price changes.
- **Sort & Filter**: Sort reports by name or price.
- **Web Interface (FastAPI)**:
  - Homepage with filterable, sortable product table
  - Price history charts
  - JSON API (`/api/products`, `/api/products/{name}`)
- **Bot Commands**:
  - `/start`, `/subscribe`, `/unsubscribe`
  - `/report`, `/reportdelta`, `/notifychange`
  - `/sort`, `/history {product}`

---

## How to Work with PriceParser

### Telegram Bot Usage

Find the bot in Telegram (e.g., t.me/PriceParserGoodBot, or @PriceParserGoodBot) or run locally (see Setup Instructions).

1. `/start` — greet the bot
2. `/subscribe` — receive hourly reports
3. `/unsubscribe` — stop updates
4. `/report` — get all product prices
5. `/reportdelta` — show only price changes
6. `/notifychange` — toggle notification mode (all vs only changes)
7. `/sort` — toggle sorting by name/price
8. `/history` — receive 7-day chart
9. `/help` - Show help message

---

### Web Interface

- Homepage: `http://localhost:8000`
  - Filter by category (e.g., `?category=Pokemon`)
  - Sort (e.g., `?sort=price`)
- Product chart: `http://localhost:8000/history/Bulbasaur`
- JSON API:
  - `/api/products` — all products
  - `/api/products?category=...` — by category
  - `/api/products/{name}` — individual product data

---

## Setup Instructions

### Create Virtual Environment
1. Clone the repository:
    ```bash
   git clone https://github.com/Rostislav62/PriceParser.git
   cd PriceParser

2. Create and activate a virtual environment:
    ```bash # Linux
   python -m venv priceparser-bot 
   source priceparser-bot/bin/activate
   .\priceparser-bot\Scripts\activate  # Windows

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


### Start the Telegram bot
1. Start the bot and parser:
    ```bash
   python main.py

### Run the web server
1. Start the web server and browser:
    ``bash
   uvicorn web_app:app --reload

## API Keys
The bot uses external services::
- Telegram Bot API: Obtain token from BotFather.
- MTP Service: Configure via .env (e.g., Gmail SMTP).


## Project Structure
PriceParser/
├── main.py                # Starts the Telegram bot and scheduler
├── handlers.py            # Telegram command logic
├── config.py              # Configuration (Telegram token, SMTP settings)
├── models.py              # ORM models (Product, Subscription)
├── utils.py               # Price saving/loading utilities
├── init_db.py             # Database initialization script
├── services/
│   ├── parser.py          # Web scraping logic
│   ├── notifier.py        # Notification logic
│   └── history.py         # Charting and historical data
├── web_app.py             # FastAPI web interface
├── templates/             # Jinja2 HTML templates
├── static/                # CSS, images, and chart output
├── requirements.txt
└── .env


## Technologies
- **Python 3.8.10**: Core language.
- **aiogram 2.21**: Telegram Bot API framework.
- **BeautifulSoup**: HTML parsing.
- **smtplib**: Email notifications.
- **requests**: HTTP requests.
- **schedule**: Periodic tasks.
- **peewee**: SQLite ORM.
- **python-dotenv**: Environment variables support.
- **FastAPI + Jinja2**: web rendering.
- **matplotlib**: charts
- **Git**: Version control.


## Author
Rostislav — Full-stack developer specializing in automation, bots, data scraping and API integration. 
This project is part of my portfolio, showcasing expertise in Telegram bots, NLP, and data automation.
Telegram: @rostislav62

## License
MIT License