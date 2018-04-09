# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/31 0031
# http://www.cnblogs.com/yuanchenqi/articles/5732581.html
import logging

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename='test.log',
                   filemode='a')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')