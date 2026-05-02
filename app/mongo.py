import os
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB", "support_agent_logs")

client = MongoClient(MONGO_URL)

db = client[MONGO_DB]

messages_collection = db["message_logs"]


def save_message_log(data):
    data["created_at"] = datetime.utcnow()
    messages_collection.insert_one(data)