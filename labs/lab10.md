#Lab 10

Part 1
```
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
```
Part 2

```
import pymongo
from bson.objectid import ObjectId
import datetime
from random import randint
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.csci2963

def findRandom():
	total = db.definitions.count();
	randomInt = randint(0,total)
	i = 0
	temp_word = "temp word"
	for word in db.definitions.find():
	    t = str(datetime.datetime.now())  
	    if i == randomInt:
	        temp_word = word["word"]      
	        db.definitions.update({"word":temp_word}, {"$push": {"dates": t}})
	        break
	    i+=1
	print ""
	print(temp_word)
	print(db.definitions.find_one({"word":temp_word}))
	print ""

if __name__ == '__main__':
	i = 0
	while(i < 10):
		findRandom()
		i += 1
```
