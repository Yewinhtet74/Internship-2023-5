import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["my_db1"]
collection=database["my_col1"]
try:
    '''
    data = {'name': 'ME', 'age': 'ME'}
    datas =[
        {'_id':8,'name': 'ME', 'age': 'ME'},
        {'_id':9,'name': 'ME', 'age': 'ME'}
    ]
    # collection.insert_one(data)
    collection.insert_many(datas)
    '''
    ids = collection.find().distinct('name')
    print(ids)
    data=collection.find_one({'name':'Ye'})
    print(data)
    for i in collection.find({'name':'Ye'},{'email':0}):
        print('Find',i)
    for i in collection.find({}, {"name": 1}):
        print('1',i)
    for i in collection.find({'_id':{'$gt':3}}):
        print('Condition',i)
    for i in collection.find({'name':None}):
        print('Condition :',i)
except Exception as err:
    print(err)