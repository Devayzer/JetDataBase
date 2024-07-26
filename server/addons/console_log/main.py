import logging

class CustomFormatter(logging.Formatter):
    
    RESET = "\033[0m"
    GREEN = "\033[32m"
    WHITE = "\033[37m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    
    FORMATS = {
        logging.INFO: GREEN + "[%(asctime)s]" + RESET + BLUE + " [%(module)s] " + RESET + "%(message)s",
        logging.WARNING: GREEN + "[%(asctime)s]" + RESET + YELLOW + " [WARNING] " + RESET + YELLOW + "%(message)s" + RESET,
        logging.ERROR: GREEN + "[%(asctime)s]" + RESET + RED + " [ERROR] " + RESET + RED + "%(message)s" + RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

def console_log(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
    
    return logger