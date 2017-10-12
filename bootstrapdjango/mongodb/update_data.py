# coding:utf-8

from pymongo import MongoClient
from bson.objectid import ObjectId

Client = MongoClient("localhost", 27017)  # db是demaxiya
db = Client.demaxiya
# collection是demaxiya
colleciton = db.demaxiya
list = colleciton.find()

for item in list:
    print item
print "========="

# colleciton.update({"Name":'gailun'},{"$set":{"Level":"4"}})
colleciton.update({"_id":ObjectId('59d726c819292b0355c45e28')},{"$set":{"Level":"5"}})

list2 = colleciton.find()

for item in list2:
    print item