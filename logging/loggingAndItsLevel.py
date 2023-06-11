import logging
''' types
DEBUG
INFO
WARNING
ERROR
CRITICAL'''
logging.basicConfig(format='%(asctime)s %(levelname)-8s:%(message)s',
                    level=logging.DEBUG,
                    filename='logs.txt',
                    datefmt='%d-%m-%Y %H:%M:%S') # to give logs of minimum if not writen in code the min is warning level that will show
logger=logging.getLogger('test')
logger.info('this is info')
logger.warning('this is not')

