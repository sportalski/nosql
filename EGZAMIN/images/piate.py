import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$group" : {"_id" : "$ticket", "prices" :{ "$sum": "$price"}}},{ "$project": {"_id": 0, "Id": "$_id", "prices": 1}}])
                                     

print(list(trades))