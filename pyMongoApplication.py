import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://XXXX@cluster0.6daxzq1.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

# inserindo informações no doc
post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as informações
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

#print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
},
    {
    "author": "Joao",
    "text": "Post from Joao. New post available",
    "title": "Mongo is fun",
    "date": datetime.datetime(2009, 11, 10, 10, 45)
    }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("_" * 45)
pprint.pprint(db.posts.find_one())
print("_" * 45)
pprint.pprint(db.posts.find_one({"author": "Joao"}))

for post in posts.find():
    pprint.pprint(post)
