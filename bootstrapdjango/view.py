# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connections
import json
import logging
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.views.decorators.csrf import csrf_exempt

log = logging.getLogger('module view.py')
log.setLevel(logging.INFO)

def showdata(request):
    dict1 = {'key1':1,'key2':2}
    dict2 ={'key1':3,'key2':4}
    data = [dict1,dict2]
    return render(request, 'login.html')


def getdata_mysql(request):
    result = []
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    departmentname = request.GET.get('departmentname')
    search = request.GET.get('search')
    print limit
    print offset
    print departmentname
    print search

    conn = connections['mysql']
    cursor = conn.cursor()
    cursor.execute("select count(*) from bootstrap_demo")
    total = cursor.fetchall()
    if search is None or search == "":
        cursor.execute("select * from bootstrap_demo limit %s, %s" % (offset, limit))
    else:
        cursor.execute("select * from bootstrap_demo bd where bd.Name='%s' limit %s, %s" % (search, offset, limit))
    db_result = cursor.fetchall()
    for item in db_result:
        #db_dict = {"ID":item[0],"Name":item[1],"ParentName":item[2],"Level":item[3],"Desc":item[4]}
        db_dict = {"ID":item[0],"Name":item[1],"ParentName":item[2],"Level":item[3]}
        result.append(db_dict)
    data2 = {'total':total,'rows':result}
    return HttpResponse(json.dumps(data2))

def getdata_mongodb(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    departmentname = request.GET.get('departmentname')
    search = request.GET.get('search')
    print limit
    print offset
    print departmentname
    print search

    total = 0
    result = []
    Client = MongoClient("localhost", 27017)
    #db是demaxiya
    db = Client.demaxiya
    #collection是demaxiya
    colleciton = db.demaxiya


    if search is None or search == "":
        total = colleciton.count()
        for data in colleciton.find().limit(int(limit)).skip(int(offset)):
            data['_id'] = str(data['_id'])
            result.append(data)
    else:
        for data in colleciton.find({"Name":search}).limit(int(limit)).skip(int(offset)):
            data['_id'] = str(data['_id'])
            result.append(data)
            total += 1
    data2 = {'total':total,'rows':result}
    return HttpResponse(json.dumps(data2))

def update_mongdb(request):
    Client = MongoClient("localhost", 27017)
    #db是demaxiya
    db = Client.demaxiya
    #collection是demaxiya
    colleciton = db.demaxiya

    colleciton.update({"_id":ObjectId('59d726c819292b0355c45e28')},{"$set":{"Level":"5"}})

@csrf_exempt
def login(request):
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    if user_name == "123" and password == "123":
        return HttpResponse(json.dumps({'SUCCESS':'success'}))
    else:
        return HttpResponse(json.dumps({'FAILED':'fail'}))

def success_login(request):
    return render(request,'demo.html')

def showselect(request):
    data1 = {"ID":"1","team":"skt","honour":"王者"}
    result = []
    result.append(data1)
    data2 = {'total':1,'rows':result}
    return HttpResponse(json.dumps(data2))