from models import Product, Subscription
from datetime import datetime

def save_prices(prices):
    for name, price in prices.items():
        Product.create(name=name, price=price, timestamp=datetime.now())

def get_latest_prices():
    latest = {}
    for product in Product.select().order_by(Product.timestamp.desc()):
        if product.name not in latest:
            latest[product.name] = product.price
    return latest

def get_previous_prices():
    latest = get_latest_prices()
    previous = {}
    for product in Product.select().order_by(Product.timestamp.desc()):
        if product.name not in latest or product.price != latest[product.name]:
            previous[product.name] = product.price
            break
    return previous

def get_subscribers():
    return [sub.user_id for sub in Subscription.select().where(Subscription.subscribed == True)]