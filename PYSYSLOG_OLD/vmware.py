import os
import pwd 
import datetime
import loggin
import re 
import grp 
import gc 
import errno
import time
import codecs
import logging.handlers

# Change the root logger level 
logging.getlogger('').setlevel(logging.NOTSET)
# Import my parsers
from parsers import vmware_syslog
# Setup logging
logging.basicConfig(filename='logs/vmware.log', level=logging.INFO, format='',datefmt='%Y-%m-%d %H:%M')

handler = logging.handlers.RotatingFileHandler(filename='logs/vmware.log', maxBytes=20000, backupCount=2)
