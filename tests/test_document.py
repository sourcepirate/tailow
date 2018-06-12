from datetime import datetime
from unittest.mock import patch, Mock
from bson.objectid import ObjectId
from .base import AioTestCase, AsyncMock
from tailow.connection import Connection
from tailow.fields import *
from tailow.document import Document

class ObjectDict(dict):
    
    def __getattribute__(self, f):
        return  self[f]

class TestModel(Document):
    a = IntegerField(required=True)
    b = IntegerField(required=True)

class TestDocument(AioTestCase):
    
    def setUp(self):
        self.objid = ObjectId.from_datetime(datetime.now())
    
    async def test_model_save(self):
        with patch('tailow.connection.Connection.get_collection', new_callable=Mock) as amock:
            new_mock = AsyncMock()
            new_mock.insert_one = insert_mock = AsyncMock(return_value=ObjectDict(inserted_id=12))
            amock.return_value = new_mock
            m = TestModel(a=1, b=2)
            await m.save()
            self.assertTrue(insert_mock.called)
            self.assertTrue(amock.called)
            self.assertIsNotNone(m._id)

    async def test_model_update_on_id_present(self):
        with patch('tailow.connection.Connection.get_collection', new_callable=Mock) as amock:
            new_mock = AsyncMock()
            new_mock.update_one = update_one = AsyncMock(return_value=ObjectDict(inserted_id=12))
            amock.return_value = new_mock
            m = TestModel(id=self.objid, a=1, b=2)
            await m.save()
            self.assertTrue(update_one.called)
            self.assertTrue(amock.called)
            self.assertIsNotNone(m._id)
    
    async def test_model_delete(self):
        with patch('tailow.connection.Connection.get_collection', new_callable=Mock) as amock:
            new_mock = AsyncMock()
            new_mock.delete_one = delete_mock = AsyncMock(return_value=True)
            amock.return_value = new_mock
            m = TestModel(id=self.objid, a=1, b=2)
            await m.delete()
            self.assertTrue(delete_mock.called)
            self.assertTrue(amock.called)