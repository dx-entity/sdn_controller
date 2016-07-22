
import logging
from oslo_log.loggers import WritableLogger


class LogFormat(object):
    def __init__(self, format_str=None, level=logging.DEBUG):
        self.format_str = format_str if format_str else '[%(asctime)s] %(name)s:%(levelname)s:'
        self.level = level

    def getLogger(self, name):

        logger = logging.getLogger(name)
        logger.setLevel(self.level)

        printer = logging.StreamHandler()
        formatter = logging.Formatter(self.format_str)
        printer.setFormatter(formatter)

        logger.addHandler(printer)

        return logger