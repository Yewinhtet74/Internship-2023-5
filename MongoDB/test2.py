import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["my_db1"]
collection=database["bussiness_info"]
try:
    '''
    q={'name':{'$regex':'^e'}}
    q1={}
    for i in collection.find(q1).sort('name',-1):
        print(i)
    '''
    q2={'Series reference':'2019.09'}
    doc={'$set':
             {'Series reference':'1.1'}
         }
    q3={'Description':{'$regex':'All'}}
    doc={'$set':{'Description':'New....'}}
    #collection.update_many(q3,doc)
    for i in collection.find().limit(3):
        print(i)
    #s=collection.replace_one({'Description':{'$regex':'New'}},{'Revised':111,'Description':'May'})
    '''
    collection.update_one({'Description':None},{'$set':{'Revised':[111,112,113]}})
    q4={'Revised':{'$size':3}}
    for i in collection.find(q4):
        print('size',i)
    '''
    q5={'$and':
        [
            {'Description': {'$in':['May',None]}},
            {'Period':None}
        ]
        }
    q6={
        '$or':
            [
                {'Revised':{'$lt':120}},
                {'Revised':{'$gt':1500}}
            ]
    }
    q7={
        'Revised':{
            '$not':{'$gt':1000}
        }
    }
    for i in collection.find(q7):
        print('Operator',i)

except Exception as err:
    print(err)