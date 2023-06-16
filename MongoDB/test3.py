import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["my_db1"]
collection=database["my_col3"]
'''
collection.insert_many( [
   { "item": "Pens", "quantity": 350, "tags": [ "school", "office" ] },
   { "item": "Erasers", "quantity": 15, "tags": [ "school", "home" ] },
   { "item": "Maps", "tags": [ "office", "storage" ] },
   { "item": "Books", "quantity": 5, "tags": [ "school", "storage", "home" ] }
] )
'''
for i in collection.find( { 'quantity': { '$in': [ 5, 15 ] } }, { '_id': 0 } ):
    print(i)