import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(LOG_FILE_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FILE_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Logging has started")
