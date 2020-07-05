""" Functions for cart management """
import logging
from logging import Logger

from flask import Flask, jsonify, request

from .core import cart as core_cart
from .utils.logger import config_logger

app = Flask(__name__)

LOGGER: Logger = config_logger(name='api.cart', level=logging.DEBUG)

@app.route('/api/cart', methods=['GET'])
def cart_list() -> str:
    """ View a user's shopping cart """
    result = core_cart.cart_list()
    cart = []
    for each in result:
        item = {
            'name': each['name'],
            'price': each['price']
        }
        cart.append(item)
    return jsonify(cart)

@app.route('/api/cart', methods=['POST'])
def cart_add() -> str:
    """ Add an item to a shopping cart """
    # TODO: implement validation
    item = request.get_json().get('item')
    result = core_cart.cart_add(item)
    if result.acknowledged:
        return jsonify({'message': 'sucess'})
    return jsonify({'message': 'error. Contact support'})

@app.route('/api/cart', methods=['DELETE'])
def cart_remove() -> str:
    """ Remove an item from a shopping cart """
    item = request.get_json().get('item')
    result = core_cart.cart_remove(item.get('name'))
    if result.acknowledged:
        return jsonify({'message': 'sucess'})
    return jsonify({'message': 'error. Contact support'})
