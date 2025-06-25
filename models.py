from peewee import Model, CharField, FloatField, DateTimeField, IntegerField, BooleanField, SqliteDatabase
from config import DATABASE_PATH
from datetime import datetime

db = SqliteDatabase(DATABASE_PATH)

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    name = CharField()
    price = FloatField()
    category = CharField(default="uncategorized")
    timestamp = DateTimeField(default=datetime.now)


class Subscription(BaseModel):
    user_id = IntegerField(unique=True)
    subscribed = BooleanField(default=True)
    notify_only_on_change = BooleanField(default=False)  # новая опция


def init_db():
    db.connect()
    db.create_tables([Product, Subscription], safe=True)
    db.close()