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

# Define the logs directory

logs_dir  = /data/vmware
processed_dir = /data/processed
processed_file_path = os.path.join(processed_dir, 'status.txt')

# Change the root logger level 
logging.getlogger('').setlevel(logging.NOTSET)
# Import my parsers
from parsers import vmware_syslog
# Setup logging
logging.basicConfig(filename='logs/vmware.log', level=logging.INFO,datefmt='%Y-%m-%d %H:%M')

handler = logging.handlers.RotatingFileHandler(filename='logs/vmware.log', maxBytes=20000, backupCount=2)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getlogger('').addHandler(handler)


# logging the start or the begining of the program 
logging.info('Pysyslog program application started')
uid = pwd.getpwnam('root').pw_uid
gid = grp.getgrnam('').gr_gid

# Identify the patters that the data starts with 

patterns = {
  r"^\d+" : vmware_syslog,
  r"^<(\d+)>\d+" : vmware_syslog,
}


# Main function 
def convert(log):
  for pattern, function in patterns.items():
    if re.search(pattern,log):
      cef_log = function(log)
      if cef_log:
        logging.info(f"log is parsed by the function")
        return cef_log, function.__name___
      else:
        logging.error(f"log is not parsed or converted")
        return None, None
  logging.error(f"No match patterns")
  return None


