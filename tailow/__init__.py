
from motor import pymongo
from tailow.connection import Connection

def connect(*args, **kwargs):
    Connection.connect(*args, **kwargs)