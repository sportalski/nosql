import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

trades = db.trades.aggregate([{"$project" : {"_id" : 0, "odnosnik" :"$details"}}])
                                     

print(list(trades))