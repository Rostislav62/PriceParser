import logging
import smtplib
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD
from utils import get_latest_prices, get_previous_prices, get_subscribers

logger = logging.getLogger(__name__)

async def notify_subscribers(bot, prices):
    if not prices:
        return
    latest = get_latest_prices()
    previous = get_previous_prices()
    report = []
    for name, price in prices.items():
        change = ""
        if name in previous and previous[name] != price:
            change = f" ({'up' if price > previous[name] else 'down'} ${abs(price - previous[name]):.2f})"
        report.append(f"Product: {name}, Price: ${price:.2f}{change}")
    report_text = "\n".join(report)

    # Telegram notifications
    for user_id in get_subscribers():
        try:
            await bot.send_message(user_id, report_text)
            logger.info(f"Sent Telegram report to {user_id}")
        except Exception as e:
            logger.error(f"Error sending Telegram report to {user_id}: {str(e)}")

    # Email notification (optional)
    if EMAIL_HOST and EMAIL_USER and EMAIL_PASSWORD:
        try:
            msg = MIMEText(report_text)
            msg['Subject'] = 'PriceParser Report'
            msg['From'] = EMAIL_USER
            msg['To'] = EMAIL_USER
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASSWORD)
                server.send_message(msg)
            logger.info("Sent email report")
        except Exception as e:
            logger.error(f"Error sending email report: {str(e)}")