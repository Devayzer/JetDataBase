import sys
import os
#import mysql.connector
#import configparser

# Додаємо каталог addons до шляху пошуку модулів
sys.path.append(os.path.join(os.path.dirname(__file__), 'addons'))

from console_log.main import console_log

# Створення логера
logger = console_log("main")

logger.info('Start JetDB Server...')