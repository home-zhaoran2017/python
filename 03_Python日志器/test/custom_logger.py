#-*- coding=utf-8 -*-
#-- 导入模块 -----------------------------------
import os
import logging
from logging.handlers import RotatingFileHandler

class LoggerConf():
    def __init__(self, log_path, log_file_name):
        formatter = logging.Formatter('---- [%(name)s] %(asctime)s %(levelname)s [%(module)s:%(funcName)s] "%(message)s"')

        log_file=os.path.join(log_path,log_file_name)
        
        self.fh = RotatingFileHandler(log_file, mode='a', maxBytes=5*1024*1024, backupCount=5)
        self.fh.setLevel(logging.DEBUG)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.ERROR)
        
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)

    @classmethod
    def getHandler(cls):
        return cls.fh, cls.ch