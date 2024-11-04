from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['Langchain_Demo']
collection = db['payload']

# Fetch all messages from MongoDB
def fetch_data():
    messages = list(collection.find())
    return messages
