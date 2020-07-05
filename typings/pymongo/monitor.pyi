"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Class to monitor a MongoDB server on a background thread."""
class MonitorBase(object):
    def __init__(self, *args, **kwargs):
        """Override this method to create an executor."""
        ...
    
    def open(self):
        """Start monitoring, or restart after a fork.

        Multiple calls have no effect.
        """
        ...
    
    def close(self):
        """Close and stop monitoring.

        open() restarts the monitor after closing.
        """
        ...
    
    def join(self, timeout: Optional[Any] = ...):
        """Wait for the monitor to stop."""
        ...
    
    def request_check(self):
        """If the monitor is sleeping, wake it soon."""
        ...
    


class Monitor(MonitorBase):
    def __init__(self, server_description, topology, pool, topology_settings):
        """Class to monitor a MongoDB server on a background thread.

        Pass an initial ServerDescription, a Topology, a Pool, and
        TopologySettings.

        The Topology is weakly referenced. The Pool must be exclusive to this
        Monitor.
        """
        ...
    
    def close(self):
        ...
    
    def _run(self):
        ...
    
    def _check_with_retry(self):
        """Call ismaster once or twice. Reset server's pool on error.

        Returns a ServerDescription.
        """
        ...
    
    def _check_once(self):
        """A single attempt to call ismaster.

        Returns a ServerDescription, or raises an exception.
        """
        ...
    
    def _check_with_socket(self, sock_info):
        """Return (IsMaster, round_trip_time).

        Can raise ConnectionFailure or OperationFailure.
        """
        ...
    


class SrvMonitor(MonitorBase):
    def __init__(self, topology, topology_settings):
        """Class to poll SRV records on a background thread.

        Pass a Topology and a TopologySettings.

        The Topology is weakly referenced.
        """
        ...
    
    def _run(self):
        ...
    
    def _get_seedlist(self):
        """Poll SRV records for a seedlist.

        Returns a list of ServerDescriptions.
        """
        ...
    


