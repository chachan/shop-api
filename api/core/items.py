""" Functions for items management """
import logging
from logging import Logger

from pymongo.cursor import Cursor
from pymongo.results import DeleteResult, InsertManyResult

from ..utils.db import connect_to_db
from ..utils.logger import config_logger

LOGGER: Logger = config_logger(name='core.items', level=logging.DEBUG)

def items_list() -> Cursor:
    """ Get a list of items for sale """
    LOGGER.debug('getting list of items')
    db = connect_to_db() # pylint: disable=invalid-name
    try:
        result = db.items.find({})
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result

def items_add(items: list) -> InsertManyResult:
    """ List a new item up for sale """
    LOGGER.debug('adding items to list of items: {}'.format([each['name'] for each in items]))
    db = connect_to_db() # pylint: disable=invalid-name
    try:
        # TODO: implement validation
        result = db.items.insert_many(items)
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result

def items_remove(item_name: str) -> DeleteResult:
    """ Unlist an item for sale """
    LOGGER.debug('removing item from list of items: {}'.format(item_name))
    db = connect_to_db() # pylint: disable=invalid-name
    try:
        result = db.items.delete_one({'name': item_name})
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result
