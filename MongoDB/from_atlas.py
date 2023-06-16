import pymongo
url='mongodb+srv://root:toor@cluster0.dk2ac3s.mongodb.net/?retryWrites=true&w=majority'

connection = pymongo.MongoClient(url)
database = connection["myDB"]
collection=database["myCollection"]
try:
    for i in collection.find():
        print(i)
except Exception as err:
    print(err)