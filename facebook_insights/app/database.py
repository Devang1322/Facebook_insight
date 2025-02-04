from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

MONGO_URI = "mongodb://localhost:27017"
try:
    client = MongoClient("mongodb://localhost:27017")
    db = client["facebook_insights"]
    print("Connected to MongoDB successfully")
except Exception as e:
    print(f"Error: {str(e)}")

try:
    client = MongoClient(MONGO_URI)
    db = client["facebook_insights"]
    pages_collection = db["pages"]
    logger.info("Connected to MongoDB")
except Exception as e:
    logger.error(f"MongoDB connection error: {e}")
    raise
