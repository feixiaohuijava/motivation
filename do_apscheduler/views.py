# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import time
from apscheduler_demo.config_apscheduler import scheduler,logger
from django.http import HttpResponse
from bootstrapdjango.settings import BASE_DIR
from datetime import datetime,date
# from apscheduler_demo.apscheduler_api import add_job
# logger.info("you are in views.py")
# logger.info(id(scheduler))

# def temp_api(*args,**kwargs):
#     print args[0]
#     print args[1]
#     print kwargs['ad']


def get_job_list(request):
    job_list = scheduler.get_jobs()
    print (job_list,job_list)
    # temp_api(1,2,ad="hanbin",ap="timo")
    # print scheduler._listeners
    return HttpResponse({"1":"2"})


# @scheduler.add_job(trigger='interval',id="tick",seconds='5')
# def tick(request):
#     print "why"
#     print('Tick! The time is: %s' % datetime.now())
#     return HttpResponse({"dema":"gailun"})


def tick():
    try:
        current_time = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
        print current_time
        file_object = open('insert_data', 'a')
        file_object.write(current_time + '\n')
    except Exception,e:
        print e
    finally:
        file_object.close()

def create_job(request):
    result = scheduler.add_job(tick,trigger='interval',seconds=10,id='insert_time')
    print ("add_job_result",result)
    return HttpResponse({"1":"2"})

def modify_job(request):
    # temp_dict = {"seconds":20}
    # temp_trigger = scheduler._create_trigger(trigger='interval',trigger_args=temp_dict)
    # result = scheduler.modify_job(job_id='insert_time',trigger=temp_trigger)
    result = scheduler.reschedule_job(job_id='insert_time',trigger='interval',seconds=20)
    print ("modify_job_result",result)
    return HttpResponse({"2":"3"})

def remove_job(request):
    """
    直接删除存储在数据库里面的任务
    :param request:
    :return:
    """
    result = scheduler.remove_all_jobs()
    logger.info(result)
    return HttpResponse({"dema":"ad"})
#
# def pause_job(request):
#     # job_list = scheduler.get_jobs()
#     # for item_job in job_list:
#     #     print item_job.id
#     # result = scheduler.pause_job(job_id='interval_print_time_three')
#     # print result
#     result = scheduler.pause_job(job_id='date_type_three')
#     logger.info(result)
#     return HttpResponse({"1":"3"})
#
#
# def resume_job(request):
#     result = scheduler.resume_job(job_id='date_type_three')
#     logger.info(result)
#     return HttpResponse({"timo":"xunjie"})





