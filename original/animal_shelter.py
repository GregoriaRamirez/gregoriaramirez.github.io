from pymongo import MongoClient  # Imports MongoDB client to interact with the database
from bson.objectid import ObjectId  # Used to reference an ObjectId in MongoDB


class DatabaseError(Exception):
    """Custom exception for database errors."""
    # Catches database errors
    pass


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        """Sets up the database connection when the class is initialized"""

        # Database connection settings
        USER = 'aacuser'         # Username for MongoDB
        PASS = 'SNHU1234'        # Password
        HOST = 'nv-desktop-services.apporto.com'  # MongoDB host address
        PORT = 32440             # Port number
        DB = 'AAC'               # Database name
        COL = 'animals'          # Collection name

        # Establish MongoDB connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def close(self):
        """Closes the MongoDB connection"""
        self.client.close()
        print("MongoDB connection closed.")

    def create(self, data):
        """Inserts a document into the database"""
        if data and isinstance(data, dict):  # Ensure data is a non-empty dictionary
            try:
                result = self.collection.insert_one(data)  # Try inserting the data
                return bool(result.inserted_id)  # True if inserted successfully
            except Exception as e:
                raise DatabaseError(f"Error inserting data: {e}")
        else:
            raise ValueError("Invalid data: must be a non-empty dictionary")

    def read(self, query={}):
        """Queries documents from the database"""
        if isinstance(query, dict):
            try:
                result = list(self.collection.find(query))  # Retrieve matching documents
                for document in result:
                    document['_id'] = str(document['_id'])  # Make _id display-friendly
                return result
            except Exception as e:
                raise DatabaseError(f"Error reading from database: {e}")
        else:
            raise ValueError("Invalid query: must be a dictionary")

    def update(self, query, update_data, multiple=False):
        """Updates document(s) in the database"""
        if not isinstance(query, dict) or not isinstance(update_data, dict):
            raise ValueError("Both query and update_data must be dictionaries.")

        try:
            if multiple:
                result = self.collection.update_many(query, {'$set': update_data})
            else:
                result = self.collection.update_one(query, {'$set': update_data})
            return result.modified_count  # Number of documents updated
        except Exception as e:
            raise DatabaseError(f"Error updating database: {e}")

    def delete(self, query, multiple=False):
        """Deletes document(s) from the database"""
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")

        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count  # Number of documents deleted
        except Exception as e:
            raise DatabaseError(f"Error deleting from database: {e}")

    def validate_field(self, field_name):
        """Validate that the field exists in the document schema"""
        sample_document = self.collection.find_one()
        if sample_document and field_name in sample_document:
            return True
        else:
            raise ValueError(f"Field '{field_name}' does not exist in the database.")

    def filter_by_rescue_type(self, rescue_type):
        """Filter animals by rescue type (e.g., 'Water Rescue')"""
        if isinstance(rescue_type, str):
            self.validate_field('rescue_type')
            query = {"rescue_type": rescue_type}
            return self.read(query)
        else:
            raise ValueError("rescue_type must be a string.")

    def filter_by_breed(self, breed):
        """Filter animals by breed (e.g., 'Labrador')"""
        if isinstance(breed, str):
            self.validate_field('breed')
            query = {"breed": {"$regex": breed, "$options": "i"}}  # Case-insensitive match
            return self.read(query)
        else:
            raise ValueError("breed must be a string.")

    def filter_by_rescue_and_breed(self, rescue_type, breed):
        """Filter animals by both rescue type and breed"""
        if isinstance(rescue_type, str) and isinstance(breed, str):
            self.validate_field('rescue_type')
            self.validate_field('breed')
            query = {
                "rescue_type": rescue_type,
                "breed": {"$regex": breed, "$options": "i"}
            }
            return self.read(query)
        else:
            raise ValueError("Both rescue_type and breed must be strings.")

    def filter_by_multiple_fields(self, **filters):
        """Filter animals by multiple fields dynamically"""
        if not filters:
            raise ValueError("At least one filter must be provided.")

        for key, value in filters.items():
            if not isinstance(value, str):
                raise ValueError(f"The value for '{key}' must be a string.")
            self.validate_field(key)

        query = {key: {"$regex": value, "$options": "i"} for key, value in filters.items()}
        return self.read(query)
