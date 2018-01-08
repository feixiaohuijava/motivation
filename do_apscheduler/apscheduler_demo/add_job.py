# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os
from pytz import utc

from apscheduler.schedulers.background import BlockingScheduler,BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED,EVENT_JOB_ERROR
import logging
logger = logging.getLogger('apscheduler.scheduler')
logger.setLevel(logging.DEBUG)  # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
logger.addHandler(h)

def tick(parameter):
    print parameter
    try:
        current_time = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
        print current_time
        file_object = open('insert_data', 'a')
        file_object.write(current_time + '\n')
    except Exception,e:
        logger.error(e)
    finally:
        file_object.close()
    # time.sleep(20)

def my_listener(event):
    if event.exception:
        logger.info('The job crashed :(')
    else:
        logger.info('The job worked :)')

if __name__ == '__main__':
    jobstores = {
        # 'mongo': MongoDBJobStore(),
        # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        'default': SQLAlchemyJobStore(url='mysql://root:root123@localhost/djangomysql')
        # 'default': RedisJobStore()
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    scheduler = BackgroundScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults,timezone='Asia/Shanghai')
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    # add_result = scheduler.add_job(tick, 'interval', seconds=5,id='blocking_interval_one_two',max_instances=3) #间隔10秒钟执行一次
    # logger.info(add_result)
    # scheduler.reschedule_job(job_id='blocking_interval',trigger='interval',seconds=10)
    # remove_result = scheduler.remove_all_jobs()
    # print ("remove_result",remove_result)
    scheduler.start()    #这里的调度任务是独立的一个线程
    #0 0 2 1 * ? *
    #0 0/30 9-17 * * ?
    #0 0 12 ? * WED
    #13 13 15 20 * ?  如果是cron table表达式，则是每个月20发生，
    scheduler_time = '13 13 15 * 2'
    re_scheduler_time = scheduler_time.split(" ")
    print type(re_scheduler_time)
    # second = re_scheduler_time[0]
    minute = re_scheduler_time[0]
    hour = re_scheduler_time[1]
    # day = '*' if re_scheduler_time[3] == '?' else re_scheduler_time[3]
    day = re_scheduler_time[2]
    month = re_scheduler_time[3]
    # day_of_week = '*' if re_scheduler_time[5] == '?' else re_scheduler_time[5]
    print re_scheduler_time[4]
    day_of_week = '*' if re_scheduler_time[4] == '*' else (int(re_scheduler_time[4])+6) % 7
    # year = re_scheduler_time[6] if len(re_scheduler_time) == 7 else None

    # print second
    print minute
    print hour
    print day
    print month
    print day_of_week
    # print year
    # 0   6
    # 1   0
    # 2   1

    add_result = scheduler.add_job(tick,trigger='cron',kwargs={"parameter":"json"},
                                   second=None,minute=minute,hour=hour,day=day,month=month,day_of_week=day_of_week,
                                   year=None,
                                   id='blocking_interval_one_two',max_instances=10) #间隔10秒钟执行一次
    logger.info(add_result)
    # remove_result = scheduler.remove_job(job_id='blocking_interval_one_two')
    # print "========"
    # remove_result = scheduler.remove_all_jobs()
    # print ("remove_result",remove_result)
    # print "========"
    # result = scheduler.get_jobs()
    # print result
    # re_result = scheduler.reschedule_job(job_id='blocking_interval',trigger='interval',seconds=10)
    # print ("re_result",result)
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')