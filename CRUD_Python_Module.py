# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 
from urllib.parse import quote_plus

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username='aacuser',password='Rose01', host='localhost', port=27017, db= 'aac', col = 'animals', auth_source=None): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        
        #everything has been updated to include ability to interfact with module 5 assignment.
        USER = quote_plus(username)
        PASS = quote_plus(password)
        
        #auth source
        if auth_source:
            uri = f"mongodb://{USER}:{PASS}@{host}:{port}/{db}?authSource={auth_source}"
        else:
            uri = f"mongodb://{USER}:{PASS}@{host}:{port}"
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(uri)
        self.database = self.client[db]
        self.collection = self.database[col]

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """ 
        Insert document
        Returns True when successful, False when failed
        """
        if not isinstance(data, dict) or not data:
            #Returns false
            return False
        try: 
            result = self.collection.insert_one(data)
            #below is a simple success signal
            return bool(result.acknowledged and result.inserted_id)
        except PyMongoError:
            #returns false
            return False

    # Create method to implement the R in CRUD.
    def read(self, query=None):
        """
        Query using find(), Not Find_one as insturucted.
        if query is None, return all docs
        """
        if query is not None and not isinstance(query, dict):
            return[]
        try:
            #uses empty{} to return all when query is None
            cursor = self.collection.find(query or {})
            #Brings in the cursor into a list to get python value
            return list(cursor)
        except PyMongoError:
            return[]
        
    #Adds the update module
    def update(self, query, update_data, many=False):
        """
        Updates one or more documents that match the query
        Well update all available documents, int is number of documents modified
        """
        #Validate inputs
        if not isinstance(query, dict) or not query:
            return 0
        if not isinstance(update_data, dict) or not update_data:
            return 0
        
        #set up the update variable
        if not any(k.startswith("$") for k in update_data.keys()):
            update_doc = {"$set": update_data}
        else:
            update_doc = update_data
            
        #Try applications
        try: 
            if many: 
                res = self.collection.update_many(query, update_doc)
            else:
                res = self.collection.update_one(query, update_doc)
            return int(res.modified_count) #returns the number of documents deleted
        #Exceptions
        except PyMongoError:
            return 0
        
    #Adds the delete functionality
    def delete(self, query, many=False):
        """
        Deletes one or more documents that match the input
        """
        #basic test entry
        if not isinstance(query, dict) or not query:
            return 0
        #try and application
        try:
            if many:
                res = self.collection.delete_many(query)
            else:
                res = self.collection.delete_one(query)
            return int(res.deleted_count) #Returns the number of documents deleted
        #Exceptions
        except PyMongoError:
            return 0