"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Represent MongoClient's configuration."""
class TopologySettings(object):
    def __init__(self, seeds: Optional[Any] = ..., replica_set_name: Optional[Any] = ..., pool_class: Optional[Any] = ..., pool_options: Optional[Any] = ..., monitor_class: Optional[Any] = ..., condition_class: Optional[Any] = ..., local_threshold_ms=..., server_selection_timeout=..., heartbeat_frequency=..., server_selector: Optional[Any] = ..., fqdn: Optional[Any] = ...):
        """Represent MongoClient's configuration.

        Take a list of (host, port) pairs and optional replica set name.
        """
        ...
    
    @property
    def seeds(self):
        """List of server addresses."""
        ...
    
    @property
    def replica_set_name(self):
        ...
    
    @property
    def pool_class(self):
        ...
    
    @property
    def pool_options(self):
        ...
    
    @property
    def monitor_class(self):
        ...
    
    @property
    def condition_class(self):
        ...
    
    @property
    def local_threshold_ms(self):
        ...
    
    @property
    def server_selection_timeout(self):
        ...
    
    @property
    def server_selector(self):
        ...
    
    @property
    def heartbeat_frequency(self):
        ...
    
    @property
    def fqdn(self):
        ...
    
    @property
    def direct(self):
        """Connect directly to a single server, or use a set of servers?

        True if there is one seed and no replica_set_name.
        """
        ...
    
    def get_topology_type(self):
        ...
    
    def get_server_descriptions(self):
        """Initial dict of (address, ServerDescription) for all seeds."""
        ...
    


