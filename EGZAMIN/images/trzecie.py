import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$project" : {"_id" : 0, "total" : {"$sum" : "$price"}}},{"$sort": { "_id": 1}}])
                                     

print(list(trades))