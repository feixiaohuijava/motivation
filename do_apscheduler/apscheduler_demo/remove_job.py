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
# def main():
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
    scheduler.start()    #这里的调度任务是独立的一个线程
    remove_result = scheduler.remove_all_jobs()
    print ("remove_result",remove_result)
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            print "sleep"
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')