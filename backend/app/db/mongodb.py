import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client[os.getenv("DATABASE_NAME")]

collection = db[os.getenv("COLLECTION_NAME")]

collection.create_index("question", unique=True)