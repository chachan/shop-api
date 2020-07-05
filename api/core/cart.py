""" Functions for cart management """
import logging
from logging import Logger

from pymongo.cursor import Cursor
from pymongo.results import InsertManyResult, InsertOneResult

from ..utils.db import connect_to_db
from ..utils.logger import config_logger
from .items import items_add, items_list, items_remove

LOGGER: Logger = config_logger(name='core.cart', level=logging.DEBUG)

def cart_list() -> Cursor:
    """ View a user's shopping cart """
    LOGGER.debug('getting list of items on shopping cart')
    db = connect_to_db() # pylint: disable=invalid-name
    try:
        result = db.cart.find({})
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result

def cart_add(item: dict) -> InsertOneResult:
    """ Add an item to a shopping cart """
    LOGGER.debug('adding item to shopping cart: {}'.format(item['name']))
    db = connect_to_db() # pylint: disable=invalid-name
    result = InsertOneResult(None, False)
    try:
        # TODO: implement validation
        items = items_list()
        for each in items:
            if item.get('name') == each['name']:
                result_remove = items_remove(each['name'])
                if result_remove.acknowledged:
                    result = db.cart.insert_one(item)
                    break
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result

def cart_remove(item_name: str) -> InsertManyResult:
    """ Remove an item from a shopping cart """
    LOGGER.debug('removing item from shopping cart: {}'.format(item_name))
    db = connect_to_db() # pylint: disable=invalid-name
    result = InsertManyResult(None, False)
    try:
        item = db.cart.find_one_and_delete({'name': item_name})
        if item:
            result = items_add([item])
    except Exception as exception:
        # TODO: use specifc exceptions. Create a custom error exception
        LOGGER.error(exception)
        raise Exception('There was a DB problem')
    return result
