import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "loan_and_property_registry")

try:
  client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
  client.admin.command('ping')
except ConnectionFailure as e:
  raise RuntimeError(f"Could not connect to MongoDB: {e}")

db = client[DB_NAME]