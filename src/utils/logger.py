import logging
import os
from datetime import datetime
import inspect

def setup_logger(name: str = None, level: int = logging.DEBUG) -> logging.Logger:
    if name is None:
        frame = inspect.currentframe().f_back
        name = frame.f_globals['__name__']

    logger = logging.getLogger(name)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(level)

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s:%(filename)s:%(lineno)d - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()