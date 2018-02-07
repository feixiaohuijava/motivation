#coding=utf-8
import logging
import multiprocessing
import logging.config

import daemon

from test import wrapper2

logger = None
pool = None

def main():
    global pool
    logger.info('@@@@@@@@@@@@@@@@@@@@@@')
    pool.map(wrapper2, [1, 2, 3, 4, 5])
    logger.info('######################')

if __name__ == '__main__':
    logger = None
    pool = None
    global logger, pool
    logging.config.fileConfig("logging.cfg")
    logger = logging.getLogger('analysis.main')
    preserve_fds = []
    loggers = logging.Logger.manager.loggerDict.values()
    for log in loggers:
        try:
            p_fds = [handler.stream for handler in log.handlers]
            preserve_fds.extend(p_fds)
        except Exception,e:
            pass
    with daemon.DaemonContext(files_preserve = preserve_fds):
        logger.info('start main function')
        pool = multiprocessing.Pool(processes = 10)
        main()