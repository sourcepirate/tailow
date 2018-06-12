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

class CursorMock(AsyncMock):
    
    def to_list(self, *args, **kwargs):
        return self.return_value

class TestModel(Document):
    a = IntegerField(required=True)
    b = IntegerField(required=True)

class TestModelQuerySet(AioTestCase):
    
    def setUp(self):
        self.oid = ObjectId.from_datetime(datetime.now())

    def test_model_filters(self):
        qs = TestModel.objects.filter(a=15)
        self.assertDictEqual(qs._filters, {"a": 15})
