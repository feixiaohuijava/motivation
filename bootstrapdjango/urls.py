"""bootstrapdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bootstrapdjango.view import *
from do_apscheduler.views import *
import logging


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^showdata/$', showdata),
    url(r'^getdata_mysql/$',getdata_mysql),
    url(r'^getdata_mongodb/$',getdata_mongodb),
    url(r'^showselect/$',showselect),
    url(r'^login/$',login),
    url(r'^success_login/$',success_login),
    url(r'^send_data_to_ajax/$',send_data_to_ajax),
    url(r'^reach_send_data_to_ajax/$',reach_send_data_to_ajax),
    url(r'^get_job_list/$',get_job_list),
    url(r'^add_job/$',create_job),
    url(r'^modify_job/$',modify_job),
    url(r'^remove_job/$',remove_job),
]

logger_urls = logging.getLogger('django.urls')
logger_urls.info("start django server and you are in urls.py ")

try:
    from do_apscheduler.apscheduler_demo import config_apscheduler
    logger.info("you are in urls.py")
    logger.info(id(scheduler))
except Exception,e:
    logger_urls.error(e)
    logger_urls.error("there is wrong in start_apscheduler when calling urls.py")