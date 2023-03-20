import os
import logging
import sys

FORMAT = "%(asctime)s - (%(name)s) - %(levelname)s - %(message)s"

logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
for handler in logger.handlers:
    logger.removeHandler(handler)

logger.addHandler(handler)

DEBUG_MODE = os.getenv("DEBUG_MODE", False)

MASTER_HOST = os.getenv('MASTER_HOST', '0.0.0.0')

MASTER_PORT = os.getenv('MASTER_PORT', 80)

PD_HOST = os.getenv('PD_HOST', '127.0.0.1')

PD_PORT = os.getenv('PD_PORT', 8001)

TH_HOST = os.getenv('TH_HOST', '127.0.0.1')

TH_PORT = os.getenv('TH_PORT', 8002)
