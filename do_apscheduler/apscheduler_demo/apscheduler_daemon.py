# coding:utf-8
import logging
import daemon

from remove_job import main
# lh = logging._handlers(
#     "/var/log/foo.log"
# )
#
# daemon_context = daemon.DaemonContext()
# daemon_context.files_preserve = [lh.stream]
# logger = logging.getLogger("daemon")
# logger = logging.getLogger("python-daemon")
# logger.setLevel(logging.DEBUG)
# h = logging.StreamHandler()
# logger.addHandler(h)
# logger

# lh = logging.FileHandler("/Users/feixiaohui/bootstrapdjango/motivation/do_apscheduler/apscheduler_demo/daemon.log").stream
#
# with daemon.DaemonContext(files_preserve=[lh]):
#     main()