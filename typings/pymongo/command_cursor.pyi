"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""CommandCursor class to iterate over command results."""
class CommandCursor(object):
    """A cursor / iterator over command cursors."""
    _getmore_class = ...
    def __init__(self, collection, cursor_info, address, retrieved=..., batch_size=..., max_await_time_ms: Optional[Any] = ..., session: Optional[Any] = ..., explicit_session: bool = ...):
        """Create a new command cursor.

        The parameter 'retrieved' is unused.
        """
        ...
    
    def __del__(self):
        ...
    
    def __die(self, synchronous: bool = ...):
        """Closes this cursor.
        """
        ...
    
    def __end_session(self, synchronous):
        ...
    
    def close(self):
        """Explicitly close / kill this cursor.
        """
        ...
    
    def batch_size(self, batch_size):
        """Limits the number of documents returned in one batch. Each batch
        requires a round trip to the server. It can be adjusted to optimize
        performance and limit data transfer.

        .. note:: batch_size can not override MongoDB's internal limits on the
           amount of data it will return to the client in a single batch (i.e
           if you set batch size to 1,000,000,000, MongoDB will currently only
           return 4-16MB of results per batch).

        Raises :exc:`TypeError` if `batch_size` is not an integer.
        Raises :exc:`ValueError` if `batch_size` is less than ``0``.

        :Parameters:
          - `batch_size`: The size of each batch of results requested.
        """
        ...
    
    def _has_next(self):
        """Returns `True` if the cursor has documents remaining from the
        previous batch."""
        ...
    
    @property
    def _post_batch_resume_token(self):
        """Retrieve the postBatchResumeToken from the response to a
        changeStream aggregate or getMore."""
        ...
    
    def __send_message(self, operation):
        """Send a getmore message and handle the response.
        """
        ...
    
    def _unpack_response(self, response, cursor_id, codec_options, user_fields: Optional[Any] = ..., legacy_response: bool = ...):
        ...
    
    def _refresh(self):
        """Refreshes the cursor with more data from the server.

        Returns the length of self.__data after refresh. Will exit early if
        self.__data is already non-empty. Raises OperationFailure when the
        cursor cannot be refreshed due to an error on the query.
        """
        ...
    
    @property
    def alive(self):
        """Does this cursor have the potential to return more data?

        Even if :attr:`alive` is ``True``, :meth:`next` can raise
        :exc:`StopIteration`. Best to use a for loop::

            for doc in collection.aggregate(pipeline):
                print(doc)

        .. note:: :attr:`alive` can be True while iterating a cursor from
          a failed server. In this case :attr:`alive` will return False after
          :meth:`next` fails to retrieve the next batch of results from the
          server.
        """
        ...
    
    @property
    def cursor_id(self):
        """Returns the id of the cursor."""
        ...
    
    @property
    def address(self):
        """The (host, port) of the server used, or None.

        .. versionadded:: 3.0
        """
        ...
    
    @property
    def session(self):
        """The cursor's :class:`~pymongo.client_session.ClientSession`, or None.

        .. versionadded:: 3.6
        """
        ...
    
    def __iter__(self):
        ...
    
    def next(self):
        """Advance the cursor."""
        ...
    
    __next__ = ...
    def _try_next(self, get_more_allowed):
        """Advance the cursor blocking for at most one getMore command."""
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    


class RawBatchCommandCursor(CommandCursor):
    _getmore_class = ...
    def __init__(self, collection, cursor_info, address, retrieved=..., batch_size=..., max_await_time_ms: Optional[Any] = ..., session: Optional[Any] = ..., explicit_session: bool = ...):
        """Create a new cursor / iterator over raw batches of BSON data.

        Should not be called directly by application developers -
        see :meth:`~pymongo.collection.Collection.aggregate_raw_batches`
        instead.

        .. mongodoc:: cursors
        """
        ...
    
    def _unpack_response(self, response, cursor_id, codec_options, user_fields: Optional[Any] = ..., legacy_response: bool = ...):
        ...
    
    def __getitem__(self, index):
        ...
    


