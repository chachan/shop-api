"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Perform aggregation operations on a collection or database."""
class _AggregationCommand(object):
    """The internal abstract base class for aggregation cursors.

    Should not be called directly by application developers. Use
    :meth:`pymongo.collection.Collection.aggregate`, or
    :meth:`pymongo.database.Database.aggregate` instead.
    """
    def __init__(self, target, cursor_class, pipeline, options, explicit_session, user_fields: Optional[Any] = ..., result_processor: Optional[Any] = ...):
        ...
    
    @property
    def _aggregation_target(self):
        """The argument to pass to the aggregate command."""
        ...
    
    @property
    def _cursor_namespace(self):
        """The namespace in which the aggregate command is run."""
        ...
    
    @property
    def _cursor_collection(self, cursor_doc):
        """The Collection used for the aggregate command cursor."""
        ...
    
    @property
    def _database(self):
        """The database against which the aggregation command is run."""
        ...
    
    @staticmethod
    def _check_compat(sock_info):
        """Check whether the server version in-use supports aggregation."""
        ...
    
    def _process_result(self, result, session, server, sock_info, slave_ok):
        ...
    
    def get_read_preference(self, session):
        ...
    
    def get_cursor(self, session, server, sock_info, slave_ok):
        ...
    


class _CollectionAggregationCommand(_AggregationCommand):
    def __init__(self, *args, **kwargs):
        ...
    
    @property
    def _aggregation_target(self):
        ...
    
    @property
    def _cursor_namespace(self):
        ...
    
    def _cursor_collection(self, cursor):
        """The Collection used for the aggregate command cursor."""
        ...
    
    @property
    def _database(self):
        ...
    


class _CollectionRawAggregationCommand(_CollectionAggregationCommand):
    def __init__(self, *args, **kwargs):
        ...
    


class _DatabaseAggregationCommand(_AggregationCommand):
    @property
    def _aggregation_target(self):
        ...
    
    @property
    def _cursor_namespace(self):
        ...
    
    @property
    def _database(self):
        ...
    
    def _cursor_collection(self, cursor):
        """The Collection used for the aggregate command cursor."""
        ...
    
    @staticmethod
    def _check_compat(sock_info):
        ...
    


