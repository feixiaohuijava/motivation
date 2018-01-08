# coding:utf-8



from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED,EVENT_JOB_ERROR,EVENT_JOB_ADDED
import logging
# logging.basicConfig()
logger = logging.getLogger('apscheduler.scheduler')
logger.setLevel(logging.DEBUG)  # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
logger.addHandler(h)

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

scheduler = BackgroundScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults,timezone=utc)

def my_listener(event):
    if event.exception:
        logger.info('The job crashed :(')
    else:
        logger.info('The job worked :)')

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

logger.info("scheduler start and you are in config_apscheduler.py")
scheduler.start()




