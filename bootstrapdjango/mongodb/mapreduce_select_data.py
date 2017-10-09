# coding:utf-8
from pymongo import MongoClient
from bson.code import Code

"""
利用mongodb的mapReduce实现查找 
1 首先查找status为active的数据，然后根据map中的user_name进行分组，在根据reduce中返回value
2 result1结果为：
        {u'_id': u'mark', u'value': 4.0}
        {u'_id': u'runoob', u'value': 1.0}
  result2的结果为:
        {u'counts': {u'input': 5, u'reduce': 1, u'emit': 5, u'output': 2},
        u'timeMillis': 125, u'ok': 1.0, u'result': u'post_total'}
"""

Client = MongoClient("localhost", 27017)
db = Client.mapreduce
colleciton = db.posts

map = Code("""
            function(){
            emit(this.user_name,1);
            }
            """
              )
reduce = Code("""
            function(key, values){
                 return Array.sum(values);
                 }
            """)

result1 = colleciton.map_reduce(map, reduce, out="post_total", query={'status':'active'})
for item in result1.find():
    print item

result2 = colleciton.map_reduce(map, reduce, full_response=True, out="post_total", query={'status': "active"})
print result2
