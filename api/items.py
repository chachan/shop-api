""" Functions for items management """
import logging
from logging import Logger

from flask import Flask, jsonify, request

from .core import items as core_items
from .utils.logger import config_logger

app = Flask(__name__)

LOGGER: Logger = config_logger(name='api.items', level=logging.DEBUG)

@app.route('/api/items', methods=['GET'])
def items_list() -> str:
    """ Get a list of items for sale """
    result = core_items.items_list()
    items = []
    for each in result:
        item = {
            'name': each['name'],
            'price': each['price']
        }
        items.append(item)
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def items_add() -> str:
    """ List a new item up for sale """
    # TODO: implement validation
    items: list = request.get_json().get('items')
    result = core_items.items_add(items)
    if result.acknowledged:
        return jsonify({'message': 'sucess'})
    return jsonify({'message': 'error. Contact support'})

@app.route('/api/items', methods=['DELETE'])
def items_remove() -> str:
    """ Unlist an item for sale """
    item = request.get_json().get('item')
    result = core_items.items_remove(item.get('name'))
    if result.acknowledged:
        return jsonify({'message': 'sucess'})
    return jsonify({'message': 'error. Contact support'})
