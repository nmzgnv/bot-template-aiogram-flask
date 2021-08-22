from datetime import datetime
from time import sleep

from loguru import logger


class DaemonConfig:
    OPERATING_HOURS = (0,)
    ERROR_COOLDOWN_TIME = 5 * 60
    COOLDOWN_TIME = 60 * 60


def daemon_init():
    while True:
        if datetime.now().hour in DaemonConfig.OPERATING_HOURS:
            try:
                pass
            except Exception as error:
                logger.error(str(error))
                sleep(DaemonConfig.ERROR_COOLDOWN_TIME)
        else:
            sleep(DaemonConfig.COOLDOWN_TIME)
