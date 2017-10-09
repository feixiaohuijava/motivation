# coding:utf-8
from pymongo import MongoClient

Client = MongoClient("localhost", 27017)
db = Client.mapreduce
colleciton = db.posts

colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "mark",
    "status": "active"
})
colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "mark",
    "status":"active"
})
colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "mark",
    "status":"active"
})
colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "mark",
    "status":"active"
})
colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "mark",
    "status":"disabled"
})
colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "runoob",
    "status":"disabled"
})

colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "runoob",
    "status":"disabled"
})

colleciton.insert({
    "post_text": "菜鸟教程，最全的技术文档。",
    "user_name": "runoob",
    "status":"active"
})



