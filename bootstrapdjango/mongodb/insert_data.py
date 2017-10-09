# coding:utf-8
from pymongo import MongoClient

Client = MongoClient("localhost", 27017)  # db是demaxiya
db = Client.demaxiya
# collection是demaxiya
colleciton = db.demaxiya

# colleciton.insert({"Name":"gailun","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"manzi","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"hanbin","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"timo","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"huangzi","ParentName":"lol","Level":"3"})


# colleciton.insert({"Name":"huli","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"dazhui","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"vn","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"delaiwen","ParentName":"lol","Level":"3"})
# colleciton.insert({"Name":"xiannv","ParentName":"lol","Level":"3"})
