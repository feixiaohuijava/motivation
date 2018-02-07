#coding=utf-8
import logging

logger = logging.getLogger('analysis.test')
def wrapper2(i):
    logger.info('wrapper2 %s' % (i))