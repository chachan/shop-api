import os

from pymongo import MongoClient


def connect_to_db() -> MongoClient:
    """ Returns Mongo db instance """
    db_url = os.environ.get('MONGODB_URL')
    db_url = 'mongodb+srv://telescoped:)7OwvXyImhn4l&;7@cluster0-oe3qq.mongodb.net/shop?retryWrites=true&w=majority'
    client = MongoClient(db_url)
    return client.shop
