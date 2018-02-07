"""
WSGI config for bootstrapdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# try:
#     from do_apscheduler.apscheduler_demo import config_apscheduler
# except ImportError,e:
#     print e

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootstrapdjango.settings")

application = get_wsgi_application()







