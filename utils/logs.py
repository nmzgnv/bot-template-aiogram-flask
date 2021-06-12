import logging
from config import DEBUG

logging_level = logging.DEBUG if DEBUG else logging.INFO

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging_level)
