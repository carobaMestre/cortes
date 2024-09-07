from loguru import logger
import sys

# Configurações básicas de logs
logger.remove()
logger.add(sys.stdout, level="INFO")

def log_error(message):
    logger.error(message)

def log_info(message):
    logger.info(message)
