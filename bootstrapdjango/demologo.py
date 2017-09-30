# coding: utf-8

__author__ = 'feixiaohui'

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#创建一个handler，用于写入文件
logfile = './log.txt'
fh = logging.FileHandler(logfile,mode='a')
fh.setLevel(logging.DEBUG)

#再次创建一个handler,用于输出到console
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

#定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#logger里面添加到handler
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("this is logger dubug message")
logger.info("this is logger info message")
logger.warning("this is logger warning message")
logger.error("this is logger error message")
logger.critical("this is logger critical message")
