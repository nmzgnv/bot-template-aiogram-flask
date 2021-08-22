from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                      CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter,
                                      CantParseEntities, MessageCantBeDeleted)
from loguru import logger

from bot.loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, CantDemoteChatCreator):
        logger.exception("Can't demote chat creator")
        return True

    if isinstance(exception, MessageNotModified):
        logger.exception('Message is not modified')
        return True
    if isinstance(exception, MessageCantBeDeleted):
        logger.exception('Message cant be deleted')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logger.exception('Message to delete not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logger.exception('MessageTextIsEmpty')
        return True

    if isinstance(exception, Unauthorized):
        logger.exception(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logger.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logger.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True
    if isinstance(exception, RetryAfter):
        logger.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True
    if isinstance(exception, CantParseEntities):
        logger.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    logger.exception(f'Update: {update} \n{exception}')
