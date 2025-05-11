import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from utils import save_prices, get_latest_prices, get_previous_prices
from services.parser import scrape_prices
from models import Subscription

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(message: types.Message, state: FSMContext):
    await state.finish()
    logger.info(f"User {message.from_user.id} started bot")
    await message.reply("Welcome to PriceParser! Use /subscribe to receive price updates or /report for the latest prices.")

async def subscribe(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    Subscription.replace(user_id=user_id, subscribed=True).execute()
    logger.info(f"User {user_id} subscribed")
    await message.reply("You are now subscribed to hourly price reports.")

async def unsubscribe(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    Subscription.replace(user_id=user_id, subscribed=False).execute()
    logger.info(f"User {user_id} unsubscribed")
    await message.reply("You have unsubscribed from price reports.")

async def report(message: types.Message, state: FSMContext):
    await state.finish()
    prices = await scrape_prices()
    if prices:
        save_prices(prices)
        latest = get_latest_prices()
        previous = get_previous_prices()
        report = []
        for name, price in prices.items():
            change = ""
            if name in previous and previous[name] != price:
                change = f" ({'up' if price > previous[name] else 'down'} ${abs(price - previous[name]):.2f})"
            report.append(f"Product: {name}, Price: ${price:.2f}{change}")
        report_text = "\n".join(report)
    else:
        report_text = "No prices available. Try again later."
    await message.reply(report_text)
    logger.info(f"Sent report to {message.from_user.id}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(subscribe, commands=['subscribe'])
    dp.register_message_handler(unsubscribe, commands=['unsubscribe'])
    dp.register_message_handler(report, commands=['report'])