import time
import logging
import logging.config
from logger_conf import LOGGING_DIC

logging.config.dictConfig(LOGGING_DIC)

logger1 = logging.getLogger("hbase")
logger2 = logging.getLogger("fund")


def test_fun():
    while True:
        logger1.info("test001")
        logger2.info("test002")

        time.sleep(1)

if __name__=="__main__":
    test_fun()
