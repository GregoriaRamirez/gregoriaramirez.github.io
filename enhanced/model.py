# Written by: Gregoria Ramirez
# Course: CS-499 Computer Science Capstone
# Description: Connects to MongoDB and retrieves data into a pandas DataFrame.

# Enhancements:

# Software Design and Engineering:
# - Replaced hardcoded credentials with environment variables using python-dotenv.
# - Set up structured logging to replace print statements.
# - Refactored database access into a reusable get_data() function for better modularity.

# Databases:
# - Implemented environment variable loading for secure credential management.
# - Added exception handling for safer MongoDB connection and query execution.
# - Ensured MongoDB client is properly closed to prevent resource leaks.

# Algorithms and Data Structures:
# - Converted raw MongoDB documents into a pandas DataFrame for use in Dash filtering and charts.

# All code originally written in February 2025 and enhanced by me for the final capstone.

# Enhancement (Software Design and Engineering): Modular imports and logging configuration
import os
import pandas as pd
import logging

# Enhancement (Databases): Secure credential loading and MongoDB connectivity
from dotenv import load_dotenv
from pymongo import MongoClient

# Enhancement (Databases): Load credentials securely from .env
load_dotenv()

# Enhancement (Software Design and Engineering): Structured logging for error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_data():
    client = None
    try:
        # Enhancement (Databases): Securely retrieve MongoDB connection settings from environment variables
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        host = os.getenv("MONGO_HOST", "localhost")
        port = int(os.getenv("MONGO_PORT", 27017))
        db_name = os.getenv("MONGO_DB")
        collection_name = os.getenv("MONGO_COL")

        # Enhancement (Software Design and Engineering): Dynamically construct MongoDB URI
        if user and password:
            uri = f"mongodb://{user}:{password}@{host}:{port}/"
        else:
            uri = f"mongodb://{host}:{port}/"

        # Enhancement (Databases): Connect to MongoDB and retrieve data
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        # Enhancement (Algorithms and Data Structures): Convert MongoDB documents into a pandas DataFrame
        mongo_data = list(collection.find())
        df = pd.DataFrame(mongo_data)

        # Enhancement (Databases): Remove internal _id field from the DataFrame
        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)

        logger.info("MongoDB data successfully retrieved.")
        return df

    except Exception as e:
        # Enhancement (Databases): Handle and log MongoDB errors safely
        logger.error(f"Error retrieving data: {e}")
        return pd.DataFrame()

    finally:
        # Enhancement (Databases): Close MongoDB connection properly
        if client:
            client.close()
