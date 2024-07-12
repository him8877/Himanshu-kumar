from config.config import mongodb
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ConfigurationError, ServerSelectionTimeoutError
from sys import exit
from bson import ObjectId
from json import dumps


class MongoDB:
    def __init__(self, collection_name):
        mongodb_uri = mongodb.get('uri')
        database = mongodb.get('database')
        collection = mongodb.get(collection_name)
        try:
            client = MongoClient(mongodb_uri)
            db = getattr(client, database)
            self.collection = db[collection]
            # self.check_connection()
        except ConfigurationError:
            print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
            exit(1)
        except ServerSelectionTimeoutError as e:
            print(e)
        except Exception as e:
            print(e)

    def read_data(self, attribute, value):
        try:
            query = {
                attribute: value
            }
            records = self.collection.find(query).limit(60)
            records = list(records)
            # List to store documents
            documents_list = []

            # Iterate over the cursor to access and collect each document
            for document in records:
                # Exclude _id field
                document.pop('_id', None)
                # Append modified document to the list
                documents_list.append(document)

            # Return the list of documents
            return documents_list
            # return records
        except OperationFailure as e:
            print(f"Operation Failure: {e}")

    def check_connection(self):
        # Create a new client and connect to the server
        client = MongoClient(mongodb.get('uri'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged the deployment. You are successfully connected to MongoDB!")
        except Exception as e:
            print(e)
