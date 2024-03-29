"""
This type stub file was generated by pyright.
"""

import struct
from bson.py3compat import PY3
from typing import Any, Optional

"""Internal network layer helper methods."""
_HAS_POLL = True
_EVENT_MASK = 0
_UNPACK_HEADER = struct.Struct("<iiii").unpack
def command(sock, dbname, spec, slave_ok, is_mongos, read_preference, codec_options, session, client, check: bool = ..., allowable_errors: Optional[Any] = ..., address: Optional[Any] = ..., check_keys: bool = ..., listeners: Optional[Any] = ..., max_bson_size: Optional[Any] = ..., read_concern: Optional[Any] = ..., parse_write_concern_error: bool = ..., collation: Optional[Any] = ..., compression_ctx: Optional[Any] = ..., use_op_msg: bool = ..., unacknowledged: bool = ..., user_fields: Optional[Any] = ...):
    """Execute a command over the socket, or raise socket.error.

    :Parameters:
      - `sock`: a raw socket instance
      - `dbname`: name of the database on which to run the command
      - `spec`: a command document as an ordered dict type, eg SON.
      - `slave_ok`: whether to set the SlaveOkay wire protocol bit
      - `is_mongos`: are we connected to a mongos?
      - `read_preference`: a read preference
      - `codec_options`: a CodecOptions instance
      - `session`: optional ClientSession instance.
      - `client`: optional MongoClient instance for updating $clusterTime.
      - `check`: raise OperationFailure if there are errors
      - `allowable_errors`: errors to ignore if `check` is True
      - `address`: the (host, port) of `sock`
      - `check_keys`: if True, check `spec` for invalid keys
      - `listeners`: An instance of :class:`~pymongo.monitoring.EventListeners`
      - `max_bson_size`: The maximum encoded bson size for this server
      - `read_concern`: The read concern for this command.
      - `parse_write_concern_error`: Whether to parse the ``writeConcernError``
        field in the command response.
      - `collation`: The collation for this command.
      - `compression_ctx`: optional compression Context.
      - `use_op_msg`: True if we should use OP_MSG.
      - `unacknowledged`: True if this is an unacknowledged command.
      - `user_fields` (optional): Response fields that should be decoded
        using the TypeDecoders from codec_options, passed to
        bson._decode_all_selective.
    """
    ...

_UNPACK_COMPRESSION_HEADER = struct.Struct("<iiB").unpack
def receive_message(sock, request_id, max_message_size=...):
    """Receive a raw BSON message or raise socket.error."""
    ...

if not PY3:
    def _receive_data_on_socket(sock, length):
        ...
    
else:
    def _receive_data_on_socket(sock, length):
        ...
    
def _errno_from_exception(exc):
    ...

class SocketChecker(object):
    def __init__(self):
        ...
    
    def socket_closed(self, sock):
        """Return True if we know socket has been closed, False otherwise.
        """
        ...
    


