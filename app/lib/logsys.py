import logging
import sys

class Log:

    def __init__(self,FileName):
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                            filename='../data/logs/muscle-{}.log'.format(FileName),
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')

    @classmethod
    def logFile(cls, text):
        logging.basicConfig()

    @classmethod
    def debug(cls, text):
        logging.debug(text)

    @classmethod
    def info(cls, text):
        logging.info(text)

    @classmethod
    def warning(cls, text):
        logging.warning(text)

    @classmethod
    def error(cls, text):
        logging.error(text)

    @classmethod
    def exit(cls):
        logging.info("-------------")
        logging.info("Terminating..")
        logging.info("-------------")
        sys.exit(2)