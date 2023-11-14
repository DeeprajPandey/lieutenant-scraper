import logging
import os
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from dotenv import load_dotenv
load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
CONSOLE_FORMATTER = logging.Formatter(
    "\033[1;32m%(levelname)s\033[1;m: \033[1;34m%(message)s\033[1;m "
    "(\033[1;33m%(funcName)s\033[1;m in \033[1;35m%(filename)s\033[1;m:\033[1;33m%(lineno)d\033[1;m)"
)
FILE_FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — "
    "%(funcName)s:%(lineno)d — %(threadName)s — %(message)s"
)

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(CONSOLE_FORMATTER)
   return console_handler

def get_file_handler(file_name="default"):
    os.makedirs(LOG_DIR, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{file_name}_{today}.log")
    
    file_handler = TimedRotatingFileHandler(log_file, when="midnight")
    file_handler.setFormatter(FILE_FORMATTER)
    
    return file_handler

def get_logger(logger_name, level=None):
    logger = logging.getLogger(logger_name)

    # user argument takes precedence (to be used for temp hacky logging)
    # default to environment variable (should always be used)
    logger.setLevel(level if level is not None else LOG_LEVEL)
    
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler("scraper"))
    
    # not necessary to propagate the error up to parent
    logger.propagate = False
    return logger
