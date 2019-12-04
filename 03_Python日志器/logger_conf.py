#-*- coding=utf-8 -*-
#-- 导入模块 -----------------------------------
import os
import logging

LOGGER_PATH='.'
HBASE_LOG_NAME="hbase.log"
FUND_LOG_NAME="fund.log"
EXTREME_LOG_NAME="extreme.log"

LOGGING_DIC = {
    "version": 1,
    
    "disable_existing_loggers": False,
    
    # 格式器
    "formatters":{
        "custom":{
            "format":'[%(asctime)s] %(levelname)s [%(module)s:%(funcName)s]:\n---- "%(message)s"\n'
        },
    },
    
    # 过滤器
    "filters":{
    },
   
    # 处理器
    "handlers":{
        "stream":{
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "custom",
        },
        
        "hbase":{
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "custom",
            "filename":os.path.join(LOGGER_PATH, HBASE_LOG_NAME),
            "maxBytes": 1024*1024*5,
            "backupCount": 5,
            "encoding": "utf-8",
        },
        
        "fund":{
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "custom",
            "filename":os.path.join(LOGGER_PATH, FUND_LOG_NAME),
            "maxBytes": 1024*1024*5,
            "backupCount": 5,
            "encoding": "utf-8",
        },
        
        "extreme":{
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "custom",
            "filename":os.path.join(LOGGER_PATH, EXTREME_LOG_NAME),
            "maxBytes": 1024*1024*5,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    
    # 日志器
    "loggers":{
        # 用于hbase thrift接口程序
        "hbase":{
            "handlers": ["stream", "hbase"],
            "level": "DEBUG",
            "propagate": True,
        },
         
        # 用于"资助"模块
        "fund":{
            "handlers": ["stream", "fund"],
            "level": "DEBUG",
            "propagate": True,
        },
         
        # 用于"极端言论"模块
        "extreme":{
            "handlers": ["stream", "extreme"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
