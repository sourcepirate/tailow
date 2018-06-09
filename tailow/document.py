# simple document

from tailow.connection import Connection
from tailow.fields.base import BaseField
from tailow.queryset import QuerySet

def with_metaclass(meta, base=object):
    """create a new base for meta class"""
    return meta("NewBase", (base,), {})

def get_fields(bases, attrs):
    """ get field attributes along """
    fields = {field_name : attrs.pop(field_name) 
                 for field_name, obj in list(attrs.items()) 
                 if isinstance(obj, BaseField) }
    for base in bases[::-1]:
        if hasattr(base, "_fields"):
            fields.update(base._fields)
    return fields

def ensure_index(f):
    """ decorate it a work around for async initialization of index """
    async def inner(self, *args, **kwargs):
        if not self.__class__._ensured_index:
            await self.__class__.create_index()
            setattr(self.__class__, '_ensured_index', True)
        return await f(self, *args, **kwargs)
    return inner
    

class DocumentMetaOptions(object):
    
    def __init__(self, ncs, opts):
        self._klass = ncs
        self._name = getattr(opts, 'name', self._klass.__name__)
        self._indexes = getattr(opts, 'indexes', [])

    @property
    def name(self):
        return self._name


class DocumentMeta(type):
    
    def __new__(mcs, name, bases, attrs):
        attrs["_fields"] = get_fields(bases, attrs)
        ncs = super(DocumentMeta, mcs).__new__(mcs, name, bases, attrs)
        qryset = QuerySet(ncs)
        meta_data = DocumentMetaOptions(ncs, getattr(ncs, 'Meta', {}))
        setattr(ncs, '_ensured_index', False)
        setattr(ncs, '_meta', meta_data)
        setattr(ncs, '_collection', meta_data.name)
        setattr(ncs, 'objects', qryset)
        return ncs

class Document(with_metaclass(DocumentMeta)):

    def __init__(self, **kwargs):

        self._values = {}
        self._id = kwargs.pop("id", kwargs.pop("_id", None))
        for key, value in kwargs.items():
            if key in self._fields:
                self._values[key] = value


    def get_field_value(self, name):
        """ get field value """
        field = self._fields[name]
        value = field.get_value(self._values.get(name, None))
        return value
    
    @classmethod
    async def create_index(cls):
        if cls._meta._indexes:
            await cls.get_collection(cls._collection).create_index(cls._meta._indexes)

    def __getattribute__(self, field_name):
        if field_name in ['_fields', '_values', "_id"]:
            return object.__getattribute__(self, field_name)
        if field_name in self._fields:
            return self._fields[field_name].to_son(self._values[field_name])
        return object.__getattribute__(self, field_name)
    
    def __setattr__(self, field_name, value):
        if field_name not in self._fields:
            object.__setattr__(self, field_name, value)
        self._values[field_name] = value

    def to_son(self):
        """ get to_son """
        _value = {}
        for key, value in self._fields.items():
            val = self.get_field_value(key)
            _value[key] = self._fields[key].to_son(val)
        return _value
    
    @classmethod
    def get_collection(cls, name):
        return Connection.get_collection(name)

    @ensure_index
    async def save(self):
        conn = self.__class__.get_collection(self._collection)
        if not self._id:
            inserted = await conn.insert_one(self.to_son())
            self._id = inserted.inserted_id
        else:
            await conn.update_one({"_id": self._id}, self.to_son())
    
    @ensure_index
    async def delete(self):
        conn = self.__class__.get_collection(self._collection)
        if self._id:
            return await conn.delete_one({"_id": self._id})
        return None