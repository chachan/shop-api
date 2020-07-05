"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Bits and pieces used by the driver that don't really fit elsewhere."""
_SHUTDOWN_CODES = frozenset([11600, 91])
_NOT_MASTER_CODES = frozenset([10107, 13435, 11602, 13436, 189]) | _SHUTDOWN_CODES
_RETRYABLE_ERROR_CODES = _NOT_MASTER_CODES | frozenset([7, 6, 89, 9001])
_UUNDER = u"_"
def _gen_index_name(keys):
    """Generate an index name from the set of fields it is over."""
    ...

def _index_list(key_or_list, direction: Optional[Any] = ...):
    """Helper to generate a list of (key, direction) pairs.

    Takes such a list, or a single key, or a single key and direction.
    """
    ...

def _index_document(index_list):
    """Helper to generate an index specifying document.

    Takes a list of (key, direction) pairs.
    """
    ...

def _check_command_response(response, msg: Optional[Any] = ..., allowable_errors: Optional[Any] = ..., parse_write_concern_error: bool = ...):
    """Check the response to a command for errors.
    """
    ...

def _check_gle_response(result):
    """Return getlasterror response as a dict, or raise OperationFailure."""
    ...

def _raise_last_write_error(write_errors):
    ...

def _raise_write_concern_error(error):
    ...

def _check_write_command_response(result):
    """Backward compatibility helper for write command error handling.
    """
    ...

def _raise_last_error(bulk_write_result):
    """Backward compatibility helper for insert error handling.
    """
    ...

def _fields_list_to_dict(fields, option_name):
    """Takes a sequence of field names and returns a matching dictionary.

    ["a", "b"] becomes {"a": 1, "b": 1}

    and

    ["a.b.c", "d", "a.c"] becomes {"a.b.c": 1, "d": 1, "a.c": 1}
    """
    ...

def _handle_exception():
    """Print exceptions raised by subscribers to stderr."""
    ...

