import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$group" : {"_id" : "$_id", "total" : {"$sum" : "$shares"}}}])
                                     

print(list(trades))