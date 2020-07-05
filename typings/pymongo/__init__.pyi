"""
This type stub file was generated by pyright.
"""

from pymongo.collection import ReturnDocument
from pymongo.common import MAX_SUPPORTED_WIRE_VERSION, MIN_SUPPORTED_WIRE_VERSION
from pymongo.cursor import CursorType
from pymongo.mongo_client import MongoClient
from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.operations import DeleteMany, DeleteOne, IndexModel, InsertOne, ReplaceOne, UpdateMany, UpdateOne
from pymongo.read_preferences import ReadPreference
from pymongo.write_concern import WriteConcern

"""Python driver for MongoDB."""
ASCENDING = 1
DESCENDING = - 1
GEO2D = "2d"
GEOHAYSTACK = "geoHaystack"
GEOSPHERE = "2dsphere"
HASHED = "hashed"
TEXT = "text"
OFF = 0
SLOW_ONLY = 1
ALL = 2
version_tuple = (3, 10, 1)
def get_version_string():
    ...

__version__ = version = get_version_string()
def has_c():
    """Is the C extension installed?"""
    ...
