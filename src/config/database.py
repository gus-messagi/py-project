from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

client = MongoClient(config["MONGO_URL"])
db = client[config["DATABASE"]]

user_collection = db["user"]