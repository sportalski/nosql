import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$group" : {"_id" : "$details", "num_t" : {"$sum" : 1}}}])
                                     

print(list(trades))