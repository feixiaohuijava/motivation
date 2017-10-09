# coding:utf-8
from pymongo import MongoClient

Client = MongoClient("localhost", 27017)  # db是demaxiya
db = Client.demaxiya
# collection是demaxiya
colleciton = db.demaxiya


colleciton.remove({"lol":"gailun"})