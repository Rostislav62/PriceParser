import logging
import requests
from bs4 import BeautifulSoup
from config import SCRAPE_URL

logger = logging.getLogger(__name__)

async def scrape_prices():
    try:
        response = requests.get(SCRAPE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('li', class_='product')
        prices = {}
        for product in products:
            name = product.find('h2', class_='woocommerce-loop-product__title').text.strip()
            price = product.find('span', class_='woocommerce-Price-amount').text.strip()
            price = float(price.replace('$', ''))
            prices[name] = price
        logger.info(f"Scraped {len(prices)} products")
        return prices
    except Exception as e:
        logger.error(f"Error scraping prices: {str(e)}")
        return {}