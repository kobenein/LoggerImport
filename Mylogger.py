import logging
from datetime import datetime

formatter = logging.Formatter( "%(asctime)s [%(levelname)s] %(message)s", "%y%m%d %H:%M:%S")

def config_logger(fh=True):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    rootLogger.addHandler(stream_handler)

    if fh:
        file_handler = logging.FileHandler(f'{datetime.now():%Y%m%d_%H%M%S}.log')
        file_handler.setFormatter(formatter)
        rootLogger.addHandler(file_handler)

    return rootLogger

if __name__ == "__main__":
    logging.debug(f'debug {__file__}')
    logging.info(f'info {__file__}')
    logging.warning(f'warning {__file__}')
    logging.error(f'error {__file__}')
    logging.critical(f'critical {__file__}')