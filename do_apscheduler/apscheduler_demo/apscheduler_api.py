# coding:utf-8

# from start_apscheduler import scheduler
# from apscheduler.events import EVENT_JOB_ERROR,EVENT_JOB_EXECUTED

# api_scheduler = scheduler


# def add_job(*args,**kwargs):
#     print kwargs
#     print args
#     def _add_job(func):
#         def wrapper(*args,**kwargs):
#             if args:
#                 print ("args",args)
#             if kwargs:
#                 print ("kwargs",kwargs)
#             r = func(*args,**kwargs)
#             return r
#         return wrapper
#     return _add_job


# def pause_job(*args,**kwargs):
#     job_id = kwargs['job_id']
#     if api_scheduler.get_job(job_id=job_id):
#         api_scheduler.pause_job(job_id="")



