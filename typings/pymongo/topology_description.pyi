"""
This type stub file was generated by pyright.
"""

from collections import namedtuple
from pymongo.server_type import SERVER_TYPE
from typing import Any, Optional

"""Represent a deployment of MongoDB servers."""
TOPOLOGY_TYPE = namedtuple('TopologyType', ['Single', 'ReplicaSetNoPrimary', 'ReplicaSetWithPrimary', 'Sharded', 'Unknown'])(*range(5))
SRV_POLLING_TOPOLOGIES = (TOPOLOGY_TYPE.Unknown, TOPOLOGY_TYPE.Sharded)
class TopologyDescription(object):
    def __init__(self, topology_type, server_descriptions, replica_set_name, max_set_version, max_election_id, topology_settings):
        """Representation of a deployment of MongoDB servers.

        :Parameters:
          - `topology_type`: initial type
          - `server_descriptions`: dict of (address, ServerDescription) for
            all seeds
          - `replica_set_name`: replica set name or None
          - `max_set_version`: greatest setVersion seen from a primary, or None
          - `max_election_id`: greatest electionId seen from a primary, or None
          - `topology_settings`: a TopologySettings
        """
        ...
    
    def check_compatible(self):
        """Raise ConfigurationError if any server is incompatible.

        A server is incompatible if its wire protocol version range does not
        overlap with PyMongo's.
        """
        ...
    
    def has_server(self, address):
        ...
    
    def reset_server(self, address):
        """A copy of this description, with one server marked Unknown."""
        ...
    
    def reset(self):
        """A copy of this description, with all servers marked Unknown."""
        ...
    
    def server_descriptions(self):
        """Dict of (address,
        :class:`~pymongo.server_description.ServerDescription`)."""
        ...
    
    @property
    def topology_type(self):
        """The type of this topology."""
        ...
    
    @property
    def topology_type_name(self):
        """The topology type as a human readable string.

        .. versionadded:: 3.4
        """
        ...
    
    @property
    def replica_set_name(self):
        """The replica set name."""
        ...
    
    @property
    def max_set_version(self):
        """Greatest setVersion seen from a primary, or None."""
        ...
    
    @property
    def max_election_id(self):
        """Greatest electionId seen from a primary, or None."""
        ...
    
    @property
    def logical_session_timeout_minutes(self):
        """Minimum logical session timeout, or None."""
        ...
    
    @property
    def known_servers(self):
        """List of Servers of types besides Unknown."""
        ...
    
    @property
    def has_known_servers(self):
        """Whether there are any Servers of types besides Unknown."""
        ...
    
    @property
    def readable_servers(self):
        """List of readable Servers."""
        ...
    
    @property
    def common_wire_version(self):
        """Minimum of all servers' max wire versions, or None."""
        ...
    
    @property
    def heartbeat_frequency(self):
        ...
    
    def apply_selector(self, selector, address, custom_selector: Optional[Any] = ...):
        ...
    
    def has_readable_server(self, read_preference=...):
        """Does this topology have any readable servers available matching the
        given read preference?

        :Parameters:
          - `read_preference`: an instance of a read preference from
            :mod:`~pymongo.read_preferences`. Defaults to
            :attr:`~pymongo.read_preferences.ReadPreference.PRIMARY`.

        .. note:: When connected directly to a single server this method
          always returns ``True``.

        .. versionadded:: 3.4
        """
        ...
    
    def has_writable_server(self):
        """Does this topology have a writable server available?

        .. note:: When connected directly to a single server this method
          always returns ``True``.

        .. versionadded:: 3.4
        """
        ...
    


_SERVER_TYPE_TO_TOPOLOGY_TYPE = { SERVER_TYPE.Mongos: TOPOLOGY_TYPE.Sharded,SERVER_TYPE.RSPrimary: TOPOLOGY_TYPE.ReplicaSetWithPrimary,SERVER_TYPE.RSSecondary: TOPOLOGY_TYPE.ReplicaSetNoPrimary,SERVER_TYPE.RSArbiter: TOPOLOGY_TYPE.ReplicaSetNoPrimary,SERVER_TYPE.RSOther: TOPOLOGY_TYPE.ReplicaSetNoPrimary }
def updated_topology_description(topology_description, server_description):
    """Return an updated copy of a TopologyDescription.

    :Parameters:
      - `topology_description`: the current TopologyDescription
      - `server_description`: a new ServerDescription that resulted from
        an ismaster call

    Called after attempting (successfully or not) to call ismaster on the
    server at server_description.address. Does not modify topology_description.
    """
    ...

def _updated_topology_description_srv_polling(topology_description, seedlist):
    """Return an updated copy of a TopologyDescription.

    :Parameters:
      - `topology_description`: the current TopologyDescription
      - `seedlist`: a list of new seeds new ServerDescription that resulted from
        an ismaster call
    """
    ...

def _update_rs_from_primary(sds, replica_set_name, server_description, max_set_version, max_election_id):
    """Update topology description from a primary's ismaster response.

    Pass in a dict of ServerDescriptions, current replica set name, the
    ServerDescription we are processing, and the TopologyDescription's
    max_set_version and max_election_id if any.

    Returns (new topology type, new replica_set_name, new max_set_version,
    new max_election_id).
    """
    ...

def _update_rs_with_primary_from_member(sds, replica_set_name, server_description):
    """RS with known primary. Process a response from a non-primary.

    Pass in a dict of ServerDescriptions, current replica set name, and the
    ServerDescription we are processing.

    Returns new topology type.
    """
    ...

def _update_rs_no_primary_from_member(sds, replica_set_name, server_description):
    """RS without known primary. Update from a non-primary's response.

    Pass in a dict of ServerDescriptions, current replica set name, and the
    ServerDescription we are processing.

    Returns (new topology type, new replica_set_name).
    """
    ...

def _check_has_primary(sds):
    """Current topology type is ReplicaSetWithPrimary. Is primary still known?

    Pass in a dict of ServerDescriptions.

    Returns new topology type.
    """
    ...

