# coding:utf-8

from pymongo import MongoClient

Client = MongoClient("localhost", 27017)  # db是demaxiya
db = Client.demaxiya
# collection是demaxiya
colleciton = db.demaxiya
search = "gailun"

list = colleciton.find({"Name":search})
print list
for item in list:
    print item
