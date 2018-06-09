
import sys
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

class ConnectionException(Exception):
    pass


class Connection(object):
    """
      Default persistable connection object
    """

    _default_client = None
    _default_database = None

    @classmethod
    def connect(cls, uri, db_name, loop=None):
        if not loop:
            loop = asyncio.get_event_loop()
        cls._default_client = AsyncIOMotorClient(uri, io_loop=loop)
        cls._default_database = cls._default_client[db_name]
    
    @classmethod
    def disconnect(cls):
        cls._default_client = None
        cls._default_database = None

    @classmethod
    def get_collection(cls, coll):
        if not cls._default_database:
            raise ConnectionException("Not conneted to database") 
        return cls._default_database[coll]