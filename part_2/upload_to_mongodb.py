import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(mongo_uri)

    # Check that the connection to MongoDB is available.
    client.admin.command("ping")
    print("Connected to MongoDB Atlas.")

    # Load data from JSON files.
    with open("part_2/authors.json", "r", encoding="utf-8") as file:
        authors = json.load(file)

    with open("part_2/qoutes.json", "r", encoding="utf-8") as file:
        quotes = json.load(file)

    print(f"Authors: {len(authors)}")
    print(f"Quotes: {len(quotes)}")

    # Select the database and collections.
    db = client["quotes"]
    authors_collection = db["authors"]
    quotes_collection = db["qoutes"]

    # Insert the data into MongoDB.
    authors_collection.insert_many(authors)
    quotes_collection.insert_many(quotes)

    print("Data successfully uploaded to MongoDB Atlas.")

except PyMongoError as error:
    print(f"MongoDB error: {error}")

finally:
    if "client" in locals():
        client.close()