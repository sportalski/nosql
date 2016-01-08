import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$unwind" : "$details.bids"}, {"$group": {"_id":"$ticket","Bids":{"$addToSet": "$details.bids"}}}])
                                     

print(list(trades))