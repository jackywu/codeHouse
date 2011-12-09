#!/usr/bin/env python
# encoding: utf-8
#
# This script is a module for logging
#
__authors__  = ['jacky wu <jacky.wucheng@gmail.com>', ]
__version__  = 1.0
__date__     = "Feb 28, 2011 11:07:17 AM"
__license__  = "GPL license"

import logging
import logging.handlers
import os.path

class Logging(object):
    def __init__(self, log_path ,logger_name):
        log_dir = os.path.dirname(log_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        keep_days = 60 #the old 60 log files will be keeped
        self.file_handler = logging.handlers.TimedRotatingFileHandler(log_path, 'D', 1, keep_days)
        self.file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

    def __del__(self):
        self.file_handler.close()
