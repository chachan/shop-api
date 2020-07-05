""" Logger Utility """
import logging
from logging import Handler
from typing import Type


def config_logger(name: str = '', level: int = logging.INFO,
                  format_str: str = '%(levelname)s - [%(processName)s(%(process)d)] [%(asctime)s] - %(filename)s:%(lineno)d: %(message)s',
                  handler: Type[Handler] = logging.StreamHandler, propagate: bool = True):
    """ returns a customized logger ready for use """
    _handler = handler()
    _handler.setFormatter(logging.Formatter(format_str))
    _logger = logging.getLogger(name)
    _logger.addHandler(_handler)
    _logger.setLevel(level)
    _logger.propagate = propagate
    return _logger
