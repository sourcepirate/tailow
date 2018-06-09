from unittest import TestCase
from unittest.mock import patch
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorClient
from tailow.connection import Connection

class TestConnection(TestCase):

    def setUp(self):
        """ setup the connection parameters """
        self.uri = "mongodb://localhost:27017"
        self.db_name = "test"

    @patch('motor.motor_asyncio.AsyncIOMotorClient')
    def test_connection_defaults(self, asyncio_mock):
        Connection.connect(self.uri, self.db_name)
        self.assertIsInstance(Connection._default_database, AsyncIOMotorDatabase)
        self.assertIsInstance(Connection._default_client, AsyncIOMotorClient)