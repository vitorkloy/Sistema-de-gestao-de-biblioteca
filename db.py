import pymongo

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/top"
 
    client = pymongo.MongoClient(CONNECTION_STRING)
 
    return client['top']