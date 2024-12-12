import os
import pwd
import datetime
import logging
import re
import grp
import gc
import errno
import time
import codecs
import logging.handlers

# Define the logs directory
logs_dir = '/data/vmware'
processed_dir = '/data/processed'
processed_file_path = os.path.join(processed_dir, 'status.txt')

# Ensure directories exist
os.makedirs(logs_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# Change the root logger level
logging.getLogger('').setLevel(logging.NOTSET)

# Import my parsers
from parsers import vmware_syslog

# Setup logging
handler = logging.handlers.RotatingFileHandler(
    filename=os.path.join(logs_dir, 'vmware.log'), maxBytes=20000, backupCount=2
)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger('').addHandler(handler)

# Logging the start of the program
logging.info('Pysyslog program application started')

# Ensure valid user and group IDs
uid = pwd.getpwnam('root').pw_uid
gid = grp.getgrnam('root').gr_gid

# Identify the patterns
patterns = {
    r"^\d+": vmware_syslog,
    r"^<(\d+)>\d+": vmware_syslog,
}

# Main function
def convert(log):
    for pattern, function in patterns.items():
        if re.search(pattern, log):
            cef_log = function(log)
            if cef_log:
                logging.info("Log is parsed by the function")
                return cef_log, function.__name__
            else:
                logging.error("Log is not parsed or converted")
                return None, None
    logging.error("No match patterns")
    return None
