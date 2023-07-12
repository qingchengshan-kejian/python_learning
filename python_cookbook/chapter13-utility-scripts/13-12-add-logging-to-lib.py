# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler)

# example function
def func():
    log.critical('a critical error!')
    log.debug('a debug message')


'''
import somelib
somelib.func()
'''