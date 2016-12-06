import pymongo
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.csci2963

#Find a single definition
print(db.definitions.find_one()) 

#Find a specific definition "chair"
print(db.definitions.find_one({"word": "chair"}))

#Find a record by object id 
print(db.definitions.find_one({ '_id': ObjectId('56fe9e22bad6b23cde07b945')}))

#Insert a new definition into the database and record that object's id
definitionId = db.definitions.insert_one({"word": "desk", "definition": "a table for studying"}).inserted_id

#Find the recently inserted object in the database
print(db.definitions.find_one({'_id': ObjectId(definitionId)}))
